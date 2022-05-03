from datetime import datetime, timedelta

import jwt
from django.conf import settings
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_rest_passwordreset.signals import reset_password_token_created
from helpers.model_helper import TrackingModel

from websystem.choices import ROLE_CHOICE

from .manager import MyUserManager


# Create your models here.
class User(AbstractUser, PermissionsMixin, TrackingModel):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    Username and password are required. Other fields are optional.
    """

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

    date_joined = models.DateTimeField(
        _("date joined"), default=timezone.now, editable=False
    )
    email_verified = models.BooleanField(
        default=False,
        help_text=("Designates whether this users email is verified. "),
    )

    photo = models.ImageField(upload_to="users", default="default.jpg")
    objects = MyUserManager()  # says how objects are created or retrived

    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.email

    @property
    def token(self):
        token = jwt.encode(
            {
                "username": self.username,
                "email": self.email,
                "exp": datetime.utcnow() + timedelta(minutes=1),
            },
            settings.SECRET_KEY,
            algorithm="HS256",
        )
        return token


@receiver(reset_password_token_created)
def password_reset_token_created(
    sender, instance, reset_password_token, *args, **kwargs
):

    email_plaintext_message = "{}?token={}".format(
        reverse("password_reset:reset-password-request"), reset_password_token.key
    )

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "cmesakh@ymail.com",
        # to:
        [reset_password_token.user.email],
    )
