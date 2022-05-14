from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must provide a valid email address"))

    def create_user(self, **fields):
        if not fields.get("username", None):
            raise ValueError(_("Users must submit a username"))

        if not fields.get("first_name", None):
            raise ValueError(_("Users must submit a first name"))

        email = fields.get("email")
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Base User Account: An email address is required"))

        user = self.model(**fields)

        user.set_password(fields.get("password"))
        fields.setdefault("is_staff", False)
        fields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user

    def create_superuser(self, **fields):
        fields.setdefault("is_staff", True)
        fields.setdefault("is_superuser", True)
        fields.setdefault("is_active", True)

        if fields.get("is_staff") is not True:
            raise ValueError(_("Superusers must have is_staff=True"))

        if fields.get("is_superuser") is not True:
            raise ValueError(_("Superusers must have is_superuser=True"))

        if not fields.get("password"):
            raise ValueError(_("Superusers must have a password"))

        email = fields.get("email")
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Admin Account: An email address is required"))

        user = self.create_user(**fields)
        user.save(using=self._db)
        return user
