# from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class InventoryAdmin(admin.ModelAdmin):
    """TODO: Docstring."""

    list_display = (
        'id',
        'name',
        'details',
        'stock_status',
        'quantity',
        'units',
        'location',
        'sublocation',
        'category',
        'subcategory',
        'committee_responsible_old',
        'committee_resp',
        'description',
        'item_comment',
        'current_donor',
        'thon_year',
        'reorderthreshold',
        'isvisibleforrequest',
        'lastupdate',
        'lastupdater',
    )
    list_filter = (
        'stock_status',
        'location',
        'category',
        'subcategory',
        'committee_responsible_old',
        'committee_resp',
        'isvisibleforrequest',
        'lastupdate',
        'lastupdater',
    )
    search_fields = ('name',)


class InventoryCategoryAdmin(admin.ModelAdmin):
    """TODO: Docstring."""

    list_display = ('id', 'name')
    search_fields = ('name',)


class InventoryLocationAdmin(admin.ModelAdmin):
    """TODO: Docstring."""

    list_display = ('id', 'name')
    search_fields = ('name',)


class InventoryStockStatusAdmin(admin.ModelAdmin):
    """TODO: Docstring."""

    list_display = ('id', 'name')
    search_fields = ('name',)


class InventorySubCategoryAdmin(admin.ModelAdmin):
    """TODO: Docstring."""

    list_display = ('id', 'category_name', 'parent_category')
    list_filter = ('parent_category',)


class SupplyDonationAdmin(admin.ModelAdmin):
    """TODO: Docstring."""

    list_display = (
        'id',
        'did',
        'oid',
        'contact_id',
        'date_added',
        'item_type',
        'quantity',
        'date_received',
        'item_name',
        'description',
        'retail_value',
        'donor_cost',
        'decided_date',
        'category',
        'contract',
        'check_number',
        'thankyou_call',
        'thankyou_date',
        'thankyou_captain',
        'received_benefit',
        'thon_year',
        'corporate_contact_name',
        'corporate_contact_email',
        'corporate_contact_phone',
        'timestamp',
    )
    list_filter = (
        'did',
        'oid',
        'date_added',
        'date_received',
        'decided_date',
        'contract',
        'thankyou_call',
        'thankyou_date',
        'thankyou_captain',
        'received_benefit',
        'timestamp',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Inventory, InventoryAdmin)
_register(models.InventoryCategory, InventoryCategoryAdmin)
_register(models.InventoryLocation, InventoryLocationAdmin)
_register(models.InventoryStockStatus, InventoryStockStatusAdmin)
_register(models.InventorySubCategory, InventorySubCategoryAdmin)
_register(models.SupplyDonation, SupplyDonationAdmin)
