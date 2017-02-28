from django.contrib import admin
from supply.models import Order


class OrderAdmin(admin.ModelAdmin):
    """Admin for Order model."""

    list_display = ['id', 'status', 'supplier', 'timestamp', 'entered_by', 'last_updated', 'last_updated_by']


admin.site.register(Order, OrderAdmin)