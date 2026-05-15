from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("FixMate Role", {"fields": ("user_type",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("FixMate Role", {"fields": ("user_type",)}),
    )

    list_display = ("id", "username", "email", "user_type", "is_staff", "is_active")

admin.site.register(User, CustomUserAdmin)