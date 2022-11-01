import uuid
from enum import unique

from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(_("name"), max_length=150, null=False, blank=False, unique=True)
    price = models.IntegerField(null=False, blank=False)
    description = models.CharField(_("name"), max_length=225, null=False, blank=False)
    inventory = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name
