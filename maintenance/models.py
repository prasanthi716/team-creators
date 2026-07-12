from django.db import models
from vehicles.models import Vehicle

class Maintenance(models.Model):
    MAINTENANCE_TYPES = [
        ('Routine', 'Routine'),
        ('Repair', 'Repair'),
        ('Inspection', 'Inspection'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Closed', 'Closed'),
    ]

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name='maintenances'
    )

    maintenance_type = models.CharField(
        max_length=50,
        choices=MAINTENANCE_TYPES,
        default='Routine'
    )

    description = models.TextField()

    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    start_date = models.DateField()

    end_date = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Open'
    )

    class Meta:
        ordering = ['-start_date', '-id']

    def __str__(self):
        return f"{self.vehicle.registration_number} - {self.maintenance_type} ({self.status})"

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        old_status = None

        if not is_new:
            try:
                old_status = Maintenance.objects.get(pk=self.pk).status
            except Maintenance.DoesNotExist:
                pass

        super().save(*args, **kwargs)

        if is_new:
            # When maintenance is created: Available -> In Shop
            if self.vehicle.status == 'Available':
                self.vehicle.status = 'In Shop'
                self.vehicle.save(update_fields=['status'])
        else:
            # When maintenance status changes to Closed: In Shop -> Available (never change Retired)
            if old_status == 'Open' and self.status == 'Closed':
                if self.vehicle.status == 'In Shop':
                    self.vehicle.status = 'Available'
                    self.vehicle.save(update_fields=['status'])
            # When maintenance status changes from Closed to Open: Available -> In Shop
            elif old_status == 'Closed' and self.status == 'Open':
                if self.vehicle.status == 'Available':
                    self.vehicle.status = 'In Shop'
                    self.vehicle.save(update_fields=['status'])

    def delete(self, *args, **kwargs):
        vehicle = self.vehicle
        super().delete(*args, **kwargs)
        # Restore vehicle to Available only if it is currently In Shop (never change Retired)
        if vehicle.status == 'In Shop':
            vehicle.status = 'Available'
            vehicle.save(update_fields=['status'])
