from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    ADMIN = 1
    MANAGER = 2
    STAFF = 3

    ROLE_CHOICES = ((ADMIN, "Admin"), (MANAGER, "Manager"), (STAFF, "Staff"))
    username = None
    email = models.EmailField(_("email address"), unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["role", "first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        return self.email
