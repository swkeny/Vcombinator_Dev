from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^projects/', include('projectview.urls')), #End point to serve up project/resource json
    url(r'^projecttree/', TemplateView.as_view(template_name='project.html')), # redirect to Mike's project.html file
    url(r'^main/', include('mainpage.urls')),
    url(r'^admin/', admin.site.urls),
]
