from __future__ import unicode_literals

from django.db import models


class Establishment(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=160)

    class Meta:
        app_label = 'establishment'
