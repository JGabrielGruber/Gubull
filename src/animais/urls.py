from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from django.conf.urls import include, url
from django.views import generic

from .views import bovino_list, bovino_create, bovino_detail, bovino_update, bovino_delete

app_name = 'animais'

urlpatterns = [
	path('bovinos/',								bovino_list,	name="list"),
	path('bovinos/create',							bovino_create,	name="create"),
	path('bovinos/<slug:identificacao>/',			bovino_detail,	name="detail"),
	path('bovinos/<slug:identificacao>/edit/',		bovino_update,	name="update"),
	path('bovinos/<slug:identificacao>/delete/',	bovino_delete,	name="delete"),
]
