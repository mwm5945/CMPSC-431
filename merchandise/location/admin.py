from django.contrib import admin
from location.models import Location


class LocationAdmin(admin.ModelAdmin):
    """Admin for Location model."""

    list_display = ['id', 'name', 'address', 'is_active']


admin.site.register(Location, LocationAdmin)