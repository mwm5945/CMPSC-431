from django.db import models


class Location(models.Model):
    """Locations for merchandise inventory."""

    name = models.CharField(max_length=255)
    address = models.ForeignKey('directory.Address', on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
