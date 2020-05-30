from django.contrib import admin
from .models import RFID

class ArduinoAdmin(admin.ModelAdmin):

	list_display        = ["__str__"]
	list_display_links  = ["__str__"]
	search_fields       = ["identificacao"]

	class Meta:
		model = RFID

admin.site.register(RFID, ArduinoAdmin)
