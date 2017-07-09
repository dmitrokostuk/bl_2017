# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sklad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kod_material', models.CharField(max_length=256, verbose_name=b'kod_m', blank=True)),
                ('nazva_materialy', models.CharField(max_length=256, verbose_name=b'nazva', blank=True)),
                ('kod_kategorii', models.CharField(max_length=256, verbose_name=b'kod_k', blank=True)),
                ('nazva_kategorii', models.CharField(max_length=256, verbose_name=b'nazva_k', blank=True)),
                ('od_vimiry', models.CharField(max_length=256, verbose_name=b'od_v', blank=True)),
                ('kod_nadhod', models.CharField(max_length=256, verbose_name=b'kod_nad', blank=True)),
                ('kilkist', models.CharField(max_length=256, verbose_name=b'kilkist', blank=True)),
                ('dataoformlenia', models.CharField(max_length=256, verbose_name=b'data', blank=True)),
                ('kod_vitraty', models.CharField(max_length=256, verbose_name=b'kod_v', blank=True)),
                ('kilkist_vitrat', models.CharField(max_length=256, verbose_name=b'kil_v', blank=True)),
                ('kod_naklad', models.CharField(max_length=256, verbose_name=b'kod_nakl', blank=True)),
            ],
        ),
    ]
