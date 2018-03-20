# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-20 09:06
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_solicitud_horas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='horas',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]