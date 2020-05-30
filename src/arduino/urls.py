from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from django.conf.urls import include, url
from django.views import generic

from rest_framework import routers

from .views import RFIDViewSet

app_name = 'arduino'

router = routers.DefaultRouter()
router.register(r'', RFIDViewSet)

urlpatterns = [
	path('', include(router.urls)),
]
