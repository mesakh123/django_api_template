from datetime import datetime, timedelta

import jwt
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from helpers.model_helper import TrackingModel

from .manager import MyUserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin, TrackingModel):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    Username and password are required. Other fields are optional.
    """

    class ROLE_CHOICE(models.TextChoices):
        ADMIN = 1, "Admin"
        MANAGER = 2, "Manager"
        EMPLOYEE = 3, "Employee"

    username_validator = UnicodeUsernameValidator()

    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)

    username = models.CharField(
        max_length=150,
        unique=True,
        help_text=(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": ("A user with that username already exists."),
        },
    )
    email = models.EmailField(_("email address"), blank=False, unique=True)

    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICE.choices, blank=True, null=True, default=7
    )
    is_staff = models.BooleanField(
        default=False,
        help_text=("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        default=True,
        help_text=(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    email_verified = models.BooleanField(
        default=False,
        help_text=("Designates whether this users email is verified. "),
    )

    photo = models.ImageField(upload_to="users", default="default.jpg")
    objects = MyUserManager()  # says how objects are created or retrived

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    @property
    def token(self):
        token = jwt.encode(
            {
                "username": self.username,
                "email": self.email,
                "exp": datetime.utcnow() + timedelta(hours=24),
            },
            settings.SECRET_KEY,
            algorithm="HS256",
        )
        return token
