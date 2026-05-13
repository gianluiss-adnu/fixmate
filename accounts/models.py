from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):

    class UserType(models.TextChoices):
        CUSTOMER = "CUSTOMER", "Customer"
        SERVICE_PROVIDER = "SERVICE_PROVIDER", "Service Provider"

    user_type = models.CharField(
        max_length=20,
        choices=UserType.choices,
        default=UserType.CUSTOMER
    )

    def __str__(self):
        return self.username