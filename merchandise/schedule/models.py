from django.db import models


class Shift(models.Model):
    """Merch employee shift."""

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    scheduled_employee = models.ForeignKey('directory.MerchandiseUser', null=True, blank=True, on_delete=models.SET_NULL)
    location = models.ForeignKey('location.Location', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Shift'
        verbose_name_plural = 'Shifts'