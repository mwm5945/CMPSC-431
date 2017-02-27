from django.db import models


class Location(models.Model):
    """Locations for merchandise inventory."""

    # id included
    name = models.CharField(max_length=255)
    address = models.ForeignKey('Address')

