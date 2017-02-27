from django.db import models


class Inventory(models.Model):
    """Inventory of a certain item."""

    quantity = models.IntegerField()
    item = models.ForeignKey('Item')
    location = models.ForeignKey('InventoryLocation')