# import datetime
# import uuid
#
# from django.db import models
# from projectview.models import Project
#
#
#
#
# class ProjectImage(models.Model):
#     image_id = models.CharField(primary_key=True, max_length=100, unique=True, default=uuid.uuid4)
#     # Todo: Change project_name to project
#     project_name = project_name = models.ForeignKey(Project)
#     image_location = models.CharField(max_length=256)
#     comment = models.CharField(max_length=4096)
#
#     def __str__(self):
#         return self.image_location
#
#     class Meta:
#         db_table = 'project_images'
#
