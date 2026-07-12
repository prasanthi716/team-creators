from django.db import models


class Vehicle(models.Model):

    VEHICLE_TYPES = [
        ('Truck', 'Truck'),
        ('Van', 'Van'),
        ('Trailer', 'Trailer'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('On Trip', 'On Trip'),
        ('In Shop', 'In Shop'),
        ('Retired', 'Retired'),
    ]

    registration_number = models.CharField(
        max_length=50,
        unique=True
    )

    vehicle_name = models.CharField(
        max_length=100
    )

    vehicle_type = models.CharField(
        max_length=50,
        choices=VEHICLE_TYPES
    )

    capacity = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    odometer = models.PositiveIntegerField(
        default=0
    )

    acquisition_cost = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Available'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.registration_number