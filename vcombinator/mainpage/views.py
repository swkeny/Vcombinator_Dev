from django.http import HttpResponse
from django.http import JsonResponse

from .models import ProjectImage


def index(request):
    ProjectImages = []

    for p in ProjectImage.objects.order_by('project_name'):
        jsonresult = {}
        jsonresult["name"] = p.project_name
        jsonresult["img"] = p.image_location
        jsonresult["comment"] = p.comment
        ProjectImages.append(jsonresult)

    return JsonResponse(ProjectImages, safe=False)



