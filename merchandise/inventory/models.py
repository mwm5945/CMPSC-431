from django.db import models


class Inventory(Model):
    """Inventory of a certain item."""

    quantity = models.IntegerField()
    item = models.ForeignKey('Item')
    location = models.ForeignKey('InventoryLocation')