from rest_framework import serializers
from issuetracker.models import Issues, Customers

class IssueSeriaizer(serializers.ModelSerializer):

    class Meta:
        model = Issues
        fields = ('name', 'status', 'category')


class CustomerSeriaizer(serializers.ModelSerializer):

    class Meta:
        model = Customers
        fields = ('name', 'budget')

