from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class UserCreationFormExtra(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


class UserChangeFormExtra(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


# Register your models here.
class UserAdminExtra(UserAdmin):
    form = UserChangeFormExtra
    add_form = UserCreationFormExtra
    readonly_fields = ["date_joined"]
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        (
            "Additional info",
            {
                "fields": (
                    "role",
                    "photo",
                )
            },
        ),
        ("Dates", {"fields": ("last_login", "date_joined")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )


admin.site.register(User, UserAdminExtra)
