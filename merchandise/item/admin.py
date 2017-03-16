from django.contrib import admin
from item.models import ItemDetails, Item, ItemCategory


class ItemDetailsAdmin(admin.ModelAdmin):
    """Admin for ItemDetails model."""

    list_display = ['id', 'name', 'is_active','category', 'description']


class ItemAdmin(admin.ModelAdmin):
    """Admin for Item model."""

    list_display = ['id', 'get_name', 'sku', 'price', 'get_is_active', 'size', 'get_category']

    def get_name(self, obj):
        return obj.details.name
        
    get_name.short_description = 'Name'
    get_name.admin_order_field = 'details__name'

    def get_is_active(self, obj):
        return obj.details.is_active
        
    get_is_active.short_description = 'Is Active'
    get_is_active.admin_order_field = 'details__is_active'

    def get_category(self, obj):
        return obj.details.category
        
    get_category.short_description = 'Category'
    get_category.admin_order_field = 'details__category'


class ItemCategoryAdmin(admin.ModelAdmin):
    """Admin for ItemCategory model."""

    list_display = ['id', 'name', 'parent']


admin.site.register(ItemDetails, ItemDetailsAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemCategory, ItemCategoryAdmin)