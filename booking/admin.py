from django.contrib import admin
from .models import Booking
from accounts.models import User
from services.models import Service

# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ("id", "customer", "service", "status", "scheduled_date")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "customer":
            kwargs["queryset"] = User.objects.filter(user_type="CUSTOMER")

        return super().formfield_for_foreignkey(db_field, request, **kwargs)