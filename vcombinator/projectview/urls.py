from django.conf.urls import url
from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^projectlist', views.projectdetails, name='projectdetails'),
    url(r'^$', views.index, name='index'),
    url(r'^submitproject$', views.submitproject, name='submitproject'),
]

