from django.db.models import Model

class Location(Model):
    """Locations for merchandise inventory."""

    # id included
    name = CharField(max_length=255)
    address = ForeignKey('Address')

