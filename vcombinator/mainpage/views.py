from django.http import HttpResponse
from django.http import JsonResponse

from .models import ProjectImage


def mainimages(request):
    ProjectImages = []
    for p in ProjectImage.objects.order_by('project_name'):
        jsonresult = {}
        #Todo: Change project_name to project on the model
        jsonresult["name"] = p.project_name.project_name
        jsonresult["img"] = p.image_location
        jsonresult["comment"] = p.comment
        ProjectImages.append(jsonresult)

    return JsonResponse(ProjectImages, safe=False)



