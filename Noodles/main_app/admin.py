from django.contrib import admin
from .models import Noodle, Manufacturer, Country

admin.site.register(Noodle)
admin.site.register(Country)
admin.site.register(Manufacturer)
