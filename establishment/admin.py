# -​*- coding: utf-8 -*​-

from __future__ import unicode_literals
from django.contrib import admin
from models.establishment import Establishment


class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email')


admin.site.register(Establishment, EstablishmentAdmin)
