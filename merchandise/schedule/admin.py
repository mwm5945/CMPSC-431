from django.contrib import admin
from schedule.models import Shift


class ShiftAdmin(admin.ModelAdmin):
    """Admin for Shift model."""

    list_display = ['id', 'scheduled_employee', 'start_time', 'end_time', 'location']


admin.site.register(Shift, ShiftAdmin)