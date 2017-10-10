import datetime
import uuid

from django.db import models
from django.utils import timezone as tz

class Resource(models.Model):
    resource_id = models.CharField(primary_key=True, max_length=100, unique=True, default=uuid.uuid4)
    resource_name= models.CharField(max_length=32)


    def __str__(self):
        return self.resource_name

    class Meta:
        db_table = 'resources'

class Project(models.Model):
    project_id = models.CharField(primary_key=True, max_length=100, unique=True, default=uuid.uuid4)
    project_name = models.CharField(max_length=64)
    project_description = models.CharField(max_length=1024)
    tech_relm = models.CharField(max_length=64, null=True)
    tech_sub_relm = models.CharField(max_length=64, null=True)
    northstar = models.CharField(max_length=64, null=True)
    #submission_date = models.DateField(default= tz.now())
    project_lead=models.ForeignKey(Resource, on_delete=models.CASCADE)
    round=models.CharField(max_length=6, null=True)
    project_accepted=models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.project_name

    class Meta:
        db_table = 'projects'


class ProjectResource(models.Model):
    relationship_id = models.CharField(primary_key=True, max_length=100, unique=True, default=uuid.uuid4)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)

    def __str__(self):
        return self.relationship_id

    class Meta:
        db_table = 'project_resources'

class Transaction(models.Model):
    TRANSACTION_TYPES = (('E', 'Expense'),
                         ('F', 'Funding'))

    TRANSACTION_SUB_TYPES = (
        ('C', 'IMFS Consulting Fee'),
        ('A', 'AWS Charges'),
        ('D', 'Data Expense'),
        ('S', 'Software Expense'),
        ('IF', 'Initial Funding'),
        ('AF', 'Additional Funding')
    )
    transaction_id = models.CharField(primary_key=True, max_length=100, unique=True, default=uuid.uuid4)
    project = models.OneToOneField(Project,on_delete=models.CASCADE, primary_key=False)
    transaction_type = models.CharField(max_length=1, choices=TRANSACTION_TYPES)
    transaction_sub_type = models.CharField(max_length=2, choices=TRANSACTION_SUB_TYPES, null=True)
    amount = models.DecimalField(null=True, blank=True, max_digits=11, decimal_places=2)

    def __str__(self):
        return self.transaction_id

    class Meta:
        db_table = 'transactions'