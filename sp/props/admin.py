from django.contrib import admin
from sp.props.models import Props

class PropAdmin(admin.ModelAdmin):
	list_display = ('maindiff')

admin.site.register(Props)