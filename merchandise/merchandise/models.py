# NEED TO CREATE SETTINGS AND UPDATE FILE STRUCTURE! ALL OF THESE MODELS WILL LIKELY BE IN SEPARATE FOLDERS

# from django.db.models import (BooleanField, CASCADE, CharField, DateField, DateTimeField, DecimalField, EmailField,
#                               ForeignKey, IntegerField, Model, PositiveSmallIntegerField, SET_NULL, SmallIntegerField,
#                               TextField)

MERCH_INVENTORY_SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large')
)

TRANSACTION_STATUS = (
    ('Paid', 'Paid'),
    ('Returned', 'Returned')

)

TRANSACTION_TYPE = (
    ('Online', 'Online'),
    ('In Store', 'In Store'),
    ('Other', 'Other')
)

ORDER_STATUS = (
    ('Ordered', 'Ordered'),
    ('In Transit', 'In Transit'),
    ('Arrived', 'Arrived'),
    ('Moved to Storage', 'Moved to Storage')
)


class ItemCategory(Model):
    """Item category."""

    # id included
    name = CharField(max_length=255)
    parent_category = ForeignKey('ItemCategory', on_delete=CASCADE)

class Item(Model):
    """Merchandise inventory."""

    #id automatically included
    sku = SmallIntegerField(null=False, blank=False)
    name = CharField(max_length=255)
    price = DecimalField(max_digits=10, decimal_places=2)
    is_active = BooleanField(required=)
    description = TextField(blank=True, null=True)
    size = CharField(max_length=11, null=True, blank=True, choices=MERCH_INVENTORY_SIZES)
    category = ForeignKey('ItemCategory', on_delete=SET_NULL)


class Address(Model):
    """Address."""

    line_one = CharField(max_length=255)
    line_two = CharField(max_lenght=255)
    city = CharField(max_length=255)
    state = CharField(max_length=2)
    zip = SmallIntegerField()


class Sale(Model):
    """Individual item sale."""

    # id inluded
    price = DecimalField(max_digits=10, decimal_places=2)
    item = ForeignKey('Item')
    transaction = ForeignKey('Transaction')


class Transaction(Model):
    """Complete transaction for a customer."""

    # id included
    status = CharField(max_length=10, null=False, blank=False, choices=TRANSACTION_STATUS)
    transaction_type = CharField(max_length=10, null=False, blank=False, choices=TRANSACTION_TYPE)
    date_time = DateTimeField(auto_now=True)
    customer = ForeignKey('Customer')
    completed_by = ForeignKey('ThinkUser')



class Order(Model):
    """Merchandise order to restock inventory."""

    status = CharField(max_length=10, choices=ORDER_STATUS)
    date = DateTimeField(auto_now=True)
    supplier = ForeignKey('Supplier', on_delete=SET_NULL)
    processed_by = ForeignKey('ThinkUser', on_delete=SET_NULL)


# class InventoryMovement(Model):
#     """Any addition, removal or movement of inventory."""



class Inventory(Model):
    """Inventory of a certain item."""

    # id included
    quantity = IntegerField()
    item = ForeignKey('Item')
    location = ForeignKey('InventoryLocation')


class InventoryLocation(Model):
    """Locations for merchandise inventory."""

    # id included
    name = CharField(max_length=255)
    address = ForeignKey('Address')


class Supplier(Model):
    """Merchandise supplier."""

    phone = CharField(max_length=10)
    name = CharField(max_length=255)
    address = ForeignKey('Address')


class Customer(Model):
    """Merchandise customers."""

    # id included
    email = EmailField()
    address = ForeignKey('Address', null=True, blank=True)


class ThinkUser(Model):
    """Merchandise user."""

    name = CharField(max_length=255)
    username = CharField(max_length=255)
    password = CharField(max_lenght=255)
    email = EmailField()


class Shift(Model):
    """Merch employee shift."""

    start_time = DateTimeField()
    end_time = DateTimeField()
    scheduled_employee = ForeignKey('ThinkUser', on_delete=SET_NULL)
    location = ForeignKey('InventoryLocation', on_delete=CASCADE)