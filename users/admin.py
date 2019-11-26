from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms import models as rooms_models

# Register your models here.


class RoomsInline(admin.TabularInline):
    model = rooms_models.Room


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    inlines = (RoomsInline,)

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                    "login_method",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
        "email_verified",
        "email_secret",
        "login_method",
    )
