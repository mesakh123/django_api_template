from django.db import models


class ROLE_CHOICE(models.IntegerChoices):
    ADMIN = 1, "Admin"
    MANAGER = 2, "Manager"
    EMPLOYEE = 3, "Employee"
