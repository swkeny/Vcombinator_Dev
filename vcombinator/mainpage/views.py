
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from projectview.models import Project


#
# def mainimages(request):
#     ProjectImages = []
#     for p in ProjectImage.objects.order_by('project_name'):
#         jsonresult = {}
#         #Todo: Change project_name to project on the model
#         jsonresult["name"] = p.project_name.project_name
#         jsonresult["img"] = p.image_location
#         jsonresult["comment"] = p.comment
#         ProjectImages.append(jsonresult)
#
#     return JsonResponse(ProjectImages, safe=False)


class mainpage(generic.ListView):
    context_object_name = 'projects'
    template_name = 'main.html'

    def get_queryset(self):

        # return Project.objects.order_by('-pub_date')[:5]
        return Project.objects.all()

