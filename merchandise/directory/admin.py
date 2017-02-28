from django.contrib import admin
from directory.models import Address, Customer, Supplier, MerchandiseUser


class AddressAdmin(admin.ModelAdmin):
    """Admin for Address model."""

    list_display = ['id', 'line_one', 'line_two', 'city', 'state', 'zip']


class CustomerAdmin(admin.ModelAdmin):
    """Admin for Customer model."""

    list_display = ['id', 'email', 'address']


class SupplierAdmin(admin.ModelAdmin):
    """Admin for Supplier model."""

    list_display = ['id', 'phone', 'name', 'address', 'is_active']


class MerchandiseUserAdmin(admin.ModelAdmin):
    """Admin for MerchandiseUser model."""

    list_display = ['id', 'username', 'first_name', 'last_name', 'last_login', 'is_superuser', 'email', 'is_staff', 'is_active', 'date_joined']


admin.site.register(Address, AddressAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(MerchandiseUser, MerchandiseUserAdmin)