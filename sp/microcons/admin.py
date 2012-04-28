from django.contrib import admin
from sp.microcons.models import MicroCons

class MicroConsAdmin(admin.ModelAdmin):
	list_display = ('thesis', 'firstcontent', 'majority')

admin.site.register(MicroCons)