from django.db.models import (BooleanField, CASCADE, CharField, DateField,
                              DateTimeField, DecimalField,
                              ForeignKey, IntegerField, Model,
                              PositiveSmallIntegerField, SET_NULL, TextField)
from django.db.models import ManyToManyField

from think_infinity.utils import get_thon_year

DONATION_ITEM_TYPE = (
    ('Monetary', 'Monetary'),
    ('Product', 'Product')
)

MERCH_INVENTORY_LOCATIONS_CHOICES = (
    ('South Annex', 'South Annex'),
    ('Store A', 'Store A'),
    ('Store C', 'Store C'),
    ('Bravo Storage', 'Bravo Storage'),
    ('Delta Storage', 'Delta Storage')
)


class Inventory(Model):
    """Inventory - Information about Inventory."""

    name = CharField(max_length=255)
    details = CharField(max_length=255)
    stock_status = ForeignKey('supply_logistics.InventoryStockStatus',
                              on_delete=CASCADE, db_column='stock')
    quantity = IntegerField()
    units = CharField(max_length=255)
    location = ForeignKey('supply_logistics.InventoryLocation',
                          on_delete=CASCADE, db_column='location')
    sublocation = CharField(max_length=255, blank=True, null=True)
    category = ForeignKey('supply_logistics.InventoryCategory',
                          on_delete=CASCADE, db_column='category')
    subcategory = ForeignKey('supply_logistics.InventorySubCategory',
                             on_delete=CASCADE, db_column='subcategory', blank=True, null=True)
    committee_responsible_old = ForeignKey('directory.CommitteePosition',
                                           on_delete=CASCADE, db_column='committee_responsible')
    committee_resp = ForeignKey('directory.ThonGroup', db_column='committee_resp',
                                blank=True, null=True)
    description = CharField(max_length=255, blank=True, null=True)
    item_comment = CharField(max_length=255, blank=True, null=True)
    current_donor = CharField(max_length=255, blank=True, null=True)
    thon_year = PositiveSmallIntegerField(default=get_thon_year())
    reorderthreshold = IntegerField(default=0, db_column='reorderThreshold')  # Field name made lowercase.
    isvisibleforrequest = BooleanField(db_column='isVisibleForRequest')  # Field name made lowercase.
    lastupdate = DateTimeField(auto_now=True)
    lastupdater = ForeignKey('directory.ThinkUser', db_column='lastupdater')

    class Meta:
        db_table = 'inventory'
        verbose_name_plural = "Inventories"


class InventoryCategory(Model):
    """InventoryCategory - Information about Inventory Categories."""

    name = CharField(max_length=255)

    class Meta:
        db_table = 'inventory_categories'
        verbose_name_plural = "InventoryCategories"


class InventoryLocation(Model):
    """InventoryLocation - Information about Inventory Locations."""

    name = CharField(max_length=255)

    class Meta:
        db_table = 'inventory_locations'


class InventoryStockStatus(Model):
    """InventoryStockStatus - Information about Inventory Stock Statuses."""

    name = CharField(max_length=255)

    class Meta:
        db_table = 'inventory_stock_statuses'
        verbose_name_plural = "InventoryStockStatuses"


class InventorySubCategory(Model):
    """InventorySubCategory - Information about Inventory Sub-Categories."""

    category_name = CharField(max_length=255)
    parent_category = ForeignKey('supply_logistics.InventoryCategory')

    class Meta:
        db_table = 'inventory_sub_categories'
        verbose_name_plural = "InventorySubCategory"


class SupplyDonation(Model):
    """SupplyDonation - Information about Supply Donations."""

    did = ForeignKey('directory.Donor', on_delete=CASCADE, db_column='did',
                     null=True, blank=True)
    oid = ForeignKey('directory.ThonGroup', on_delete=CASCADE, db_column='oid',
                     null=True, blank=True)
    contact_id = IntegerField(blank=True, null=True)
    date_added = DateField(auto_now_add=True)
    item_type = CharField(max_length=8, default='Monetary', choices=DONATION_ITEM_TYPE)
    quantity = IntegerField()
    date_received = DateField(blank=True, null=True)
    item_name = CharField(max_length=255, blank=True, null=True)
    description = TextField(blank=True, null=True)
    retail_value = DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    donor_cost = DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    decided_date = DateField(blank=True, null=True)
    category = CharField(max_length=255, blank=True, null=True)
    contract = BooleanField()
    check_number = CharField(max_length=255, blank=True, null=True)
    thankyou_call = BooleanField()
    thankyou_date = DateField(null=True, blank=True)
    thankyou_captain = ForeignKey('directory.ThinkUser', on_delete=SET_NULL, blank=True, null=True,
                                  db_column='thankyou_captain')
    received_benefit = BooleanField()
    thon_year = PositiveSmallIntegerField(default=get_thon_year())
    corporate_contact_name = CharField(max_length=255, blank=True, null=True)
    corporate_contact_email = CharField(max_length=255, blank=True, null=True)
    corporate_contact_phone = CharField(max_length=255, blank=True, null=True)
    timestamp = DateTimeField(auto_now=True)

    class Meta:
        db_table = 'donor_donations'


class MerchandiseInventory(Model):
    """MerchandiseInventory - information about a merchandise inventory item"""

    item = ForeignKey('supply_logistics.MerchandiseInventoryItem')
    locations = ManyToManyField('supply_logistics.MerchandiseInventoryLocation')
    total_on_hand = PositiveSmallIntegerField(default=0)

    class Meta:
        permissions = (
            ('can_remove_change_items', 'Can Remove or Change items'),
            ('can_manage_merchandise_inventory', 'Can manage merchandise inventory'),
            ('can_use_pos_see_inventory', 'Can use POS system and see inventory'),
        )


class MerchandiseInventoryItem(Model):
    """MerchandiseItemInventory - inventory of merchandise at their respective locations."""

    thon_year_added = PositiveSmallIntegerField(default=get_thon_year(), null=False, blank=False)
    item_name = CharField(max_length=255, null=False, blank=False)
    item_id = IntegerField(null=False, blank=False)
    item_description = TextField()
    item_price = DecimalField(max_digits=10, decimal_places=2)
    is_active = BooleanField(default=True)


class MerchandiseInventoryLocation(Model):
    """MerchandiseInventoryLocation - Table for inventory locations."""

    name = CharField(max_length=255)
    quantity = PositiveSmallIntegerField(default=0)
    is_active = BooleanField(default=True)


class MerchandiseInventoryMovements(Model):
    """MerchandiseInventoryMovements - records information about each inventory movement."""

    thon_year = PositiveSmallIntegerField(get_thon_year())
    item_id = ForeignKey('supply_logistics.MerchandiseInventoryItem', on_delete=SET_NULL, null=True, blank=False)
    item_amount = PositiveSmallIntegerField(default=0, null=False, blank=False)
    from_location = CharField(max_length=14, choices=MERCH_INVENTORY_LOCATIONS_CHOICES, blank=False)
    to_location = CharField(max_length=14, choices=MERCH_INVENTORY_LOCATIONS_CHOICES, blank=False)
    user = ForeignKey('directory.ThinkUser', on_delete=CASCADE)
    timestamp = DateTimeField(blank=True, null=True, auto_now_add=True)
    description = TextField()

    class Meta:
        permissions = (
            ('can_move_merchandise_inventory', 'Can Move Merchandise Inventory'),
        )


# class AlternativeTransportationBus(Model):
#     """AlternativeTransportationBus - information about an alternative transportation bus."""
#
#     name = CharField(max_length=255)
#     is_outgoing_trip = BooleanField(default=True)  # If false, it's a return trip
#     canning_weekend = ForeignKey('directory.Event', on_delete=CASCADE)
#     stops = ManyToManyField('solicitation.AlternativeTransportationBusStopLocation',
#                             through='solicitation.AlternativeTransportationBusStop')
#
#     class Meta:
#         verbose_name_plural = 'AlternativeTransportationBuses'
#
#     def __str__(self):
#         """string representation of class returns name."""
#         return self.name
#
#
# class AlternativeTransportationBusStopLocation(Model):
#     """AlternativeTransportationStopLocation - information about a stop an alternative transportation bus will make."""
#
#     stop_loc_name = CharField(max_length=255)
#     stop_street_addr = CharField(max_length=255)
#     stop_addr_city = CharField(max_length=255)
#     stop_addr_state = CharField(max_length=2)
#     stop_addr_zip = PositiveIntegerField()
#     is_active = BooleanField(default=True)
#
#     def __str__(self):
#         """string representation of class returns name."""
#         return self.stop_loc_name
#
#
# class AlternativeTransportationBusStop(Model):
#     """AlternativeTransportationBusStop - Mapping of busses to stops with times."""
#
#     bus = ForeignKey('solicitation.AlternativeTransportationBus', related_name='_bus')
#     location = ForeignKey('solicitation.AlternativeTransportationBusStopLocation', related_name='_bus_loc')
#     date_time = DateTimeField()
#     is_outgoing_trip = BooleanField(default=True)
#
#
# class AlternativeTransportationTicketRequest(Model):
#     """AlternativeTransportationTicketRequest - individual ticket requests from users."""
#
#     user_for_ticket = ForeignKey('directory.ThinkUser', on_delete=CASCADE, related_name='_ticket_user')
#     submitter = ForeignKey('directory.ThinkUser', on_delete=CASCADE, related_name='_ticket_submitter')
#     timestamp = DateTimeField(auto_now_add=True)
#     canning_trip = ForeignKey('solicitation.CanningTrip', on_delete=CASCADE)
#     destination = ForeignKey('solicitation.AlternativeTransportationBusStopLocation', on_delete=CASCADE)
#     departure_buses = ManyToManyField('solicitation.AlternativeTransportationBus', related_name='_departure_buses')
#     return_buses = ManyToManyField('solicitation.AlternativeTransportationBus', related_name='_return_buses')
#     comments = CharField(max_length=1000, blank=True)