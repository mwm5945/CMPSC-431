from diango.db.models import Model


class Shift(Model):
    """Merch employee shift."""

    start_time = DateTimeField()
    end_time = DateTimeField()
    scheduled_employee = ForeignKey('ThinkUser', on_delete=SET_NULL)
    location = ForeignKey('InventoryLocation', on_delete=CASCADE)