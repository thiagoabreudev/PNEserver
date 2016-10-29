from django.contrib import admin
from models.establishment import Establishment


class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')


admin.site.register(Establishment, EstablishmentAdmin)
