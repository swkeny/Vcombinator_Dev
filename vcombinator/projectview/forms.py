from django import forms
from .models import Project


class ProjectSubmitForm(forms.ModelForm):
    error_css_class = 'error'

    

    class Meta:

        model = Project
        #fields = "__all__"
        fields = ['project_name', 'project_description', 'tech_relm', 'tech_sub_relm', 'northstar', 'project_lead']


