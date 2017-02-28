from django.contrib import admin
from item.models import Item, ItemCategory


class ItemAdmin(admin.ModelAdmin):
    """Admin for Item model."""

    list_display = ['id', 'name', 'description', 'sku', 'price', 'is_active', 'size', 'category']


class ItemCategoryAdmin(admin.ModelAdmin):
    """Admin for ItemCategory model."""

    list_display = ['id', 'name', 'parent']


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemCategory, ItemCategoryAdmin)