from django.db import models
from django.urls import reverse
from django.contrib import admin
from dateutil.relativedelta import relativedelta
from datetime import date, datetime
import os

class RFID(models.Model):
	identificacao	= models.AutoField(primary_key=True)
	brinco			= models.CharField(max_length=255)
	data			= models.DateTimeField(auto_now_add=True, blank=True)

	def __unicode__(self):
		return self.identificacao

	def __str__(self):
		return str(self.identificacao)

	def get_absolute_url(self):
		return reverse('arduino:detail', kwargs={'identificacao': self.identificacao})
