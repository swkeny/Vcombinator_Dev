from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .forms import ProjectSubmitForm, ProjectResourceSubmitForm
from django.forms import inlineformset_factory
from django.forms import modelformset_factory

from .models import Project, Resource, ProjectResource


def index(request):
    wrapper = []
    json_result = {}
    json_result["name"] = "Projects" # Root Level
    projects = [] # Initialize Projects list. We will append projects to this to keep track of
                  # which ones we've seen
    first_level = [] # We will attach this list of Resources (Children) to the Root Level
    for prk in ProjectResource.objects.order_by('-project_id'):
        if (prk.project.project_name not in projects):
            projects.append(prk.project.project_name)
            second_level = {}
            children = []

            second_level_team_members = {}
            second_level_project_page = {}
            second_level_list = []
            second_level_team_members["name"] = "Team Members"
            second_level_project_page["name"] = "Project Page"
            second_level_project_page["url"] = 'http://www.google.com'
            second_level["name"] = prk.project.project_name

            children_dictionary = {}
            children_dictionary["name"] = prk.resource.resource_name

            children.append(children_dictionary)
            second_level_team_members["_children"] = children

            second_level_list.append(second_level_team_members)
            second_level_list.append(second_level_project_page)

            second_level["_children"] = second_level_list
            first_level.append(second_level)
        else:
            if prk.resource.resource_name not in second_level["_children"][0]["_children"]:
                children_dictionary = {}
                children_dictionary["name"] = prk.resource.resource_name
                second_level["_children"][0]["_children"].append(children_dictionary)

    json_result["_children"] = first_level
    wrapper.append(json_result)
    return JsonResponse(wrapper, safe=False)

def projectdetails(request):
    project_list = Project.objects.order_by('-submission_date')
    template = loader.get_template('projectlist.html')
    context = {
        'project_list': project_list,
    }
    return HttpResponse(template.render(context, request))

def submitproject(request):
    if request.method == "POST":
        form = ProjectSubmitForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            response = redirect('submitprojectresource')
            response['Location'] += '?project=' + project.project_id.urn[9:]
            return response




    else:
        form = ProjectSubmitForm()
    return render(request, 'projectview/submitproject.html', {
        'form': form
    })



def submitprojectresource(request):
    if request.method == "POST":
        form = ProjectResourceSubmitForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()


    else:
        form = ProjectResourceSubmitForm()
        for key in request.GET:
            try:
                form.fields[key].initial = request.GET[key]
            except KeyError:
                # Ignore unexpected parameters
                pass
    return render(request, 'projectview/submitprojectresource.html', {
        'form': form
    })

def projectdetails(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'projectdetails.html', {'project': project})
