from django.db import models
from accounts.models import User

# Create your models here.

class Service(models.Model):
    provider = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='services'
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.provider.username}"