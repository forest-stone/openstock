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
                ('stockCode', models.CharField(serialize=False, max_length=10, primary_key=True)),
                ('now', models.IntegerField(blank=True, null=True)),
                ('recommendNum', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
