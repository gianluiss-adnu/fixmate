from django.contrib import admin
from .models import Service
from accounts.models import User


# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "provider", "price", "is_active")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "provider":
            kwargs["queryset"] = User.objects.filter(user_type="SERVICE_PROVIDER")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)