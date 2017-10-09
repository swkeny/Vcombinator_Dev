from django.contrib import admin
from .models import Resource, Project, Transaction, ProjectResource

# Register your models here.
admin.site.register(Resource)
admin.site.register(Project)
admin.site.register(Transaction)
admin.site.register(ProjectResource)