# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('establishment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='establishment',
            name='email',
            field=models.CharField(default='', max_length=120, blank=True),
        ),
        migrations.AddField(
            model_name='establishment',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128, null=True, blank=True),
        ),
    ]
