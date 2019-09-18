# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-15 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgetportal', '0025_add-infraproject-bigint-fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infrastructureprojectpart',
            name='gps_code',
        ),
        migrations.AddField(
            model_name='infrastructureprojectpart',
            name='provinces',
            field=models.CharField(default=b'', max_length=510),
        ),
    ]
