from django.db import models


class Driver(models.Model):

    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('On Trip', 'On Trip'),
        ('Suspended', 'Suspended'),
    ]


    name = models.CharField(
        max_length=100
    )

    license_number = models.CharField(
        max_length=50,
        unique=True
    )

    license_expiry = models.DateField()

    contact_number = models.CharField(
        max_length=15
    )

    safety_score = models.IntegerField(
        default=100
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
        return self.name