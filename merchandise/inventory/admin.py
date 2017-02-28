from django.contrib import admin
from inventory.models import Inventory, InventoryTransaction


class InventoryAdmin(admin.ModelAdmin):
    """Admin for Inventory model."""

    list_display = ['id', 'item', 'quantity', 'location']


class InventoryTransactionAdmin(admin.ModelAdmin):
    """Admin for InventoryTransaction model."""

    list_display = ['id', 'inventory', 'quantity', 'timestamp', 'user']


admin.site.register(Inventory, InventoryAdmin)
admin.site.register(InventoryTransaction, InventoryTransactionAdmin)