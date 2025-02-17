from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile

from django.contrib.auth import get_user_model

User = get_user_model()

# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = User
    ordering = ["id"]
    list_display = [
        "email",
        "id",
        "type",
        "is_active",
        "is_staff",
        "is_superuser",
        "is_verified",
    ]
    list_filter = ["email", "type", "is_active", "is_staff", "is_superuser", "is_verified"]
    fieldsets = (
        ("Authentications", {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "is_verified")},),
        ("group permissions", {"fields": ("groups", "user_permissions", "type")}),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_verified",
                    "type",
                ),
            },
        ),
    )


class CustomProfileAdmin(admin.ModelAdmin):
    model = Profile
    ordering = ["id"]
    list_display = ["user", "id", "first_name", "last_name"]
    searching_fields = ["id", "user", "first_name", "last_name"]


admin.site.register(Profile, CustomProfileAdmin)
admin.site.register(User, CustomUserAdmin)
# admin.site.register(UserType)