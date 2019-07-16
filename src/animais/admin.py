from django.contrib import admin
from .models import Bovino, Filhos

class BovinoAdmin(admin.ModelAdmin):

	list_display        = ["__str__", "updated", "timestamp"]
	list_display_links  = ["__str__"]
	list_filter         = ["updated", "timestamp"]
	search_fields       = ["identificacao"]

	class Meta:
		model = Bovino

admin.site.register(Bovino, BovinoAdmin)

class FilhosAdmin(admin.ModelAdmin):

	list_display        = ["__str__"]

	class Meta:
		model = Filhos

admin.site.register(Filhos, FilhosAdmin)
