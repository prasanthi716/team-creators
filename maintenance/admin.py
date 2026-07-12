from django.contrib import admin
from .models import Maintenance

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = (
        'vehicle',
        'maintenance_type',
        'status',
        'start_date',
        'end_date',
        'cost',
    )
    search_fields = (
        'vehicle__registration_number',
        'vehicle__vehicle_name',
    )
    list_filter = (
        'status',
        'maintenance_type',
        'start_date',
    )
    ordering = ('-start_date', '-id')
