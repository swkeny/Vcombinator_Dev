from django import forms
from .models import Project, ProjectResource


class ProjectSubmitForm(forms.ModelForm):
    error_css_class = 'error'



    class Meta:

        model = Project
        #fields = "__all__"
        fields = ['project_name', 'project_description', 'tech_relm', 'tech_sub_relm', 'northstar']


class ProjectResourceSubmitForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = ProjectResource
        fields = ["project", "resource"]

