# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-20 09:02
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180320_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='horas',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
