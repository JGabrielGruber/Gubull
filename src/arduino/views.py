from django.shortcuts   import render, get_object_or_404, redirect
from django.http        import HttpResponse, HttpResponseRedirect
from django.contrib     import messages
from django.http        import JsonResponse
from rest_framework.mixins import (
	CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet
from .models            import RFID
from .serializers       import RFIDSerializer

import logging, logging.config
import sys


class RFIDViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin):
	queryset = RFID.objects.all()
	serializer_class = RFIDSerializer

def arduino_list(request):
	data	= list(RFID.objects.values())
	return JsonResponse(data, safe=False)

def arduino_create(request):
	form		= RFIDForm(request.POST or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(form.get_absolute_url())
	return form
