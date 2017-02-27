from django.db.models import Model

class Inventory(Model):
    """Inventory of a certain item."""

    quantity = IntegerField()
    item = ForeignKey('Item')
    location = ForeignKey('InventoryLocation')