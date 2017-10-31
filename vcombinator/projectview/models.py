import datetime
import uuid

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone as tz

class Resource(models.Model):
    resource_id = models.CharField(primary_key=True, max_length=100, unique=True, default=uuid.uuid4)
    resource_name= models.CharField(max_length=32)


    def __str__(self):
        return self.resource_name

    class Meta:
        db_table = 'resources'

class Project(models.Model):

    TECH_REALM = (
        ('DATA', 'Data Analytics'),
        ('PLAT', 'Platforms/Visualizations'),
        ('INFRA', 'Market Infrastructure'),
    )

    TECH_SUB_REALM = (
        ('DLT', 'Distributed Ledger Technology'),
        ('ML', 'Machine Learning'),
        ('DA', 'Data Analytics'),
        ('AR', 'Augmented Reality'),
        ('VR', 'Virtual Reality'),
    )

    NORTH_STAR = (
        ('alpha', 'New Sources of Alpha'),
        ('cost', 'Lower Cost to Invest'),
        ('markets', 'Enable New Markets'),
        ('risk', 'Eliminate Uncompensated Risk'),
        ('structure', 'New Market Structures'),
        ('culture', 'Build and Enable Innovative Culture'),
    )
    project_id = models.CharField(primary_key=True, max_length=100, unique=True, default=uuid.uuid4)
    project_name = models.CharField(max_length=64)
    project_description = models.TextField(max_length=2048)
    tech_realm = models.CharField(max_length=64, null=True, choices=TECH_REALM)
    tech_sub_realm = models.CharField(max_length=64, null=True, choices =TECH_SUB_REALM )
    northstar = models.CharField(max_length=64, null=True, choices=NORTH_STAR)
    submission_date = models.DateField(default= tz.now())
    round=models.CharField(max_length=6, null=True)
    project_accepted=models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.project_name

    def get_team_members(self):
        project_resources = ProjectResource.objects.filter(project_id=self.project_id)
        return project_resources

    def get_team_member_names(self):
        project_resources = ProjectResource.objects.filter(project_id=self.project_id)
        return [pr.resource.resource_name for pr in project_resources]

    def get_team_member_names_str(self):
        project_resources = ProjectResource.objects.filter(project_id=self.project_id)
        team_names_list = [pr.resource.resource_name for pr in project_resources]
        team_names_str = ", ".join(team_names_list)
        return team_names_str

    class Meta:
        db_table = 'projects'


class ProjectResource(models.Model):
    relationship_id = models.CharField(primary_key=True, max_length=100, unique=True, default=uuid.uuid4)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    project_lead = models.BooleanField(default=False, null=False)

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

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user')

    def create_profile(sender, **kwargs):
        user = kwargs["instance"]
        if kwargs["created"]:
            user_profile = UserProfile(user=user)
            user_profile.save()

    post_save.connect(create_profile, sender=User)


