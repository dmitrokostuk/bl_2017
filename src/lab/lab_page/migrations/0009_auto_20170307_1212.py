# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 12:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab_page', '0008_auto_20170306_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='travels',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lab_page.Travels'),
        ),
    ]
