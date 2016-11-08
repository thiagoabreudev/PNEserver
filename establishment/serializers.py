# -​*- coding: utf-8 -*​-

from __future__ import unicode_literals
from rest_framework import serializers
from models.establishment import Establishment


class EstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establishment
        fields = ('name', 'address', 'phone', 'email')
