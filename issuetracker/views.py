from issuetracker.models import Customers, Issues
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import list_route
from django.db.models import Count, Max
from issuetracker.models import StatusMixin, TypeMixin
from issuetracker.serializers import CustomerSeriaizer, IssueSeriaizer

class CustomerViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin):
    queryset = Customers.objects
    serializer_class = CustomerSeriaizer


class IsuuetrackerViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Issues.objects
    serializer_class = IssueSeriaizer

    @list_route(methods=['get'], url_path='status')
    def list_status(self, request):
        counts = self.queryset.values('status').order_by('status').annotate(Count('status'))
        total = sum([c['status__count'] for c in counts])

        payload = dict([(s, 0) for s in StatusMixin.STATUS_LIST])

        for count in counts:
            if count['status__count'] > 0:
                payload[count['status']] = round(float(count['status__count']) / float(total) * 100, 2)

        return Response(payload)

    @list_route(methods=['get'], url_path='type')
    def list_types(self, request):
        counts = self.queryset.values('category').order_by('category').annotate(Count('category'))
        total = sum([c['category__count'] for c in counts])

        payload = dict([(s, 0) for s in TypeMixin.TYPE_LIST])

        for count in counts:
            if count['category__count'] > 0:
                payload[count['category']] = round(float(count['category__count']) / float(total) * 100, 2)

        return Response(payload)