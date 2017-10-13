from django import forms
from .models import Project, ProjectResource

TECH_REALM = (
    ('DATA', 'Data Analytics'),
    ('PLAT', 'Platforms/Visualization'),
    ('INFRA', 'Market Infrastructure'),
)

class ProjectSubmitForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:

        model = Project
        #fields = "__all__"
        fields = ['project_name', 'project_description', 'tech_relm', 'tech_sub_relm', 'northstar', 'project_lead']
        tech_realm = forms.ChoiceField(choices=TECH_REALM, required=True)

class ProjectResourceSubmitForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = ProjectResource
        fields = ["project", "resource"]


