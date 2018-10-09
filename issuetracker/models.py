from django.db import models


class StatusMixin(object):
    STATUS_Resolved = 'Resolved'
    STATUS_In_Progress = 'In Progress'
    STATUS_To_Be_Resolved = 'To Be Resolved'

    STATUS_LIST = [ STATUS_Resolved, STATUS_In_Progress, STATUS_To_Be_Resolved]

class TypeMixin(object):
    TYPE_Valid = 'Valid'
    TYPE_Duplicate = 'Dupicate'
    STATUS_Invalid = 'Invalid'

    TYPE_LIST = [ TYPE_Valid, TYPE_Duplicate, STATUS_Invalid]

class Customers(models.Model):
    name = models.CharField(max_length=255)
    budget = models.IntegerField()


class Issues(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default=StatusMixin.STATUS_To_Be_Resolved)
    category = models.CharField(max_length=255, default='')
    amount = models.IntegerField(null=True, blank=True)
    payment_status = models.CharField(max_length=255, default='')
    company = models.ForeignKey(Customers, null=True, blank=True, on_delete=models.CASCADE)







