from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from django.conf.urls import include, url
from django.views import generic

from rest_framework import routers

from .views import bovino_list, bovino_create, bovino_detail, bovino_update, bovino_delete, peso_add

app_name = 'animais'

urlpatterns = [
	path('', RedirectView.as_view(url='bovinos/')),
	path('bovinos/',								bovino_list,	name="list"),
	path('bovinos/create',							bovino_create,	name="create"),
	path('bovinos/<slug:identificacao>/',			bovino_detail,	name="detail"),
	path('bovinos/<slug:identificacao>/edit/',		bovino_update,	name="update"),
	path('bovinos/<slug:identificacao>/delete/',	bovino_delete,	name="delete"),
	path('bovinos/<slug:identificacao>/peso/',		peso_add,		name="peso"),
]
