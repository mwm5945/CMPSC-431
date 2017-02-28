from django.db import models


class Shift(models.Model):
    """Merch employee shift."""

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    scheduled_employee = models.ForeignKey('directory.MerchandiseUser', on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey('location.Location', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Shift'
        verbose_name_plural = 'Shifts'