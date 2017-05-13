# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('url', models.URLField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('leadingPeriod', models.IntegerField()),
                ('leadingType', models.CharField(max_length=10)),
                ('stockNum', models.IntegerField()),
                ('stockCode', models.CharField(max_length=20)),
                ('stockNow', models.CharField(max_length=30)),
                ('createDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
