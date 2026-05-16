from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Address

# Register your models here.

class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "email")}),
        ("FixMate Role", {"fields": ("user_type",)}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "first_name", "last_name", "email", "password1", "password2", "user_type"),
        }),
    )

    list_display = ("id", "username", "email", "user_type", "is_staff", "is_active")

admin.site.register(User, CustomUserAdmin)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "street", "city", "postal_code", "created_at")