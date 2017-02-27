from django.db import models


class Shift(Model):
    """Merch employee shift."""

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    scheduled_employee = models.ForeignKey('ThinkUser', on_delete=SET_NULL)
    location = models.ForeignKey('InventoryLocation', on_delete=CASCADE)