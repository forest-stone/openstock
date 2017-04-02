# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stock',
            fields=[
                ('stockCode', models.CharField(primary_key=True, max_length=10, serialize=False)),
                ('now', models.IntegerField()),
                ('diff', models.IntegerField(blank=True, null=True)),
                ('rate', models.FloatField(blank=True, null=True)),
                ('high', models.IntegerField(blank=True, null=True)),
                ('low', models.IntegerField(blank=True, null=True)),
                ('quant', models.IntegerField(blank=True, null=True)),
                ('marketSum', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
