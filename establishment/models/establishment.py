# -​*- coding: utf-8 -*​-

from __future__ import unicode_literals
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Establishment(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=160)
    phone = PhoneNumberField(null=True, blank=True, default=None)
    email = models.CharField(max_length=120, null=False, blank=True, default='')

    class Meta:
        app_label = 'establishment'
