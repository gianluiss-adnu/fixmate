from django.db import models
from accounts.models import User
from services.models import Service
from accounts.models import Address

# Create your models here.
class Booking(models.Model):

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        ACCEPTED = "ACCEPTED", "Accepted"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        COMPLETED = "COMPLETED", "Completed"
        CANCELLED = "CANCELLED", "Cancelled"

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE
    )

    scheduled_date = models.DateField()
    scheduled_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.username} - {self.service.name} ({self.status})"