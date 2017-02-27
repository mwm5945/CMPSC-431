from django.db import models


class ItemCategory(Model):
    """Item category."""

    # id included
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey('ItemCategory', on_delete=CASCADE)

class Item(Model):
    """Merchandise inventory."""

    MERCH_INVENTORY_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large')
    )

    #id automatically included
    sku = models.SmallIntegerField(null=False, blank=False)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(required=)
    description = models.TextField(blank=True, null=True)
    size = models.CharField(max_length=11, null=True, blank=True, choices=MERCH_INVENTORY_SIZES)
    category = models.ForeignKey('ItemCategory', on_delete=SET_NULL)


class Address(Model):
    """Address."""

    line_one = models.CharField(max_length=255)
    line_two = models.CharField(max_lenght=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zip = models.SmallIntegerField()


class Sale(Model):
    """Individual item sale."""

    # id inluded
    price = models.DecimalField(max_digits=10, decimal_places=2)
    item = models.ForeignKey('Item')
    transaction = models.ForeignKey('Transaction')


class Transaction(Model):
    """Complete transaction for a customer."""

    TRANSACTION_STATUS = (
        ('Paid', 'Paid'),
        ('Returned', 'Returned')

    )

    TRANSACTION_TYPE = (
        ('Online', 'Online'),
        ('In Store', 'In Store'),
        ('Other', 'Other')
    )

    # id included
    status = models.CharField(max_length=10, null=False, blank=False, choices=TRANSACTION_STATUS)
    transaction_type = models.CharField(max_length=10, null=False, blank=False, choices=TRANSACTION_TYPE)
    date_time = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey('Customer')
    completed_by = models.ForeignKey('ThinkUser')



class Order(Model):
    """Merchandise order to restock inventory."""

    ORDER_STATUS = (
        ('Ordered', 'Ordered'),
        ('In Transit', 'In Transit'),
        ('Arrived', 'Arrived'),
        ('Moved to Storage', 'Moved to Storage')
    )

    status = models.CharField(max_length=10, choices=ORDER_STATUS)
    date = models.DateTimeField(auto_now=True)
    supplier = models.ForeignKey('Supplier', on_delete=SET_NULL)
    processed_by = models.ForeignKey('ThinkUser', on_delete=SET_NULL)


# class InventoryMovement(Model):
#     """Any addition, removal or movement of inventory."""



class Inventory(Model):
    """Inventory of a certain item."""

    # id included
    quantity = models.IntegerField()
    item = models.ForeignKey('Item')
    location = models.ForeignKey('InventoryLocation')


class InventoryLocation(Model):
    """Locations for merchandise inventory."""

    # id included
    name = models.CharField(max_length=255)
    address = models.ForeignKey('Address')


class Supplier(Model):
    """Merchandise supplier."""

    phone = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    address = models.ForeignKey('Address')


class Customer(Model):
    """Merchandise customers."""

    # id included
    email = models.EmailField()
    address = models.ForeignKey('Address', null=True, blank=True)


class ThinkUser(Model):
    """Merchandise user."""

    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_lenght=255)
    email = models.EmailField()


class Shift(Model):
    """Merch employee shift."""

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    scheduled_employee = models.ForeignKey('ThinkUser', on_delete=SET_NULL)
    location = models.ForeignKey('InventoryLocation', on_delete=CASCADE)