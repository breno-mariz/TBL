# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-28 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TBLSessions', '0006_auto_20180127_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tblsession',
            name='grat_available',
        ),
        migrations.AddField(
            model_name='tblsession',
            name='grat_datetime',
            field=models.DateTimeField(blank=True, help_text='Date and time to provide the gRAT test.', null=True, verbose_name='gRAT date'),
        ),
    ]
