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
                ('title', models.CharField(max_length=10)),
                ('url', models.URLField(primary_key=True, serialize=False)),
                ('stockNum', models.IntegerField()),
                ('stock1Code', models.CharField(max_length=10)),
                ('stock2Code', models.CharField(null=True, max_length=10)),
                ('stock3Code', models.CharField(null=True, max_length=10)),
                ('createDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
