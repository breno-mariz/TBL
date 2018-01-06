# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-02 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TBLSessions', '0002_remove_tblsession_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblsession',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Date that the session is created.', verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='tblsession',
            name='is_closed',
            field=models.BooleanField(default=False, help_text='Close TBL session.', verbose_name='Is closed?'),
        ),
        migrations.AlterField(
            model_name='tblsession',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Date that the session is updated.', verbose_name='Updated at'),
        ),
    ]