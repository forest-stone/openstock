# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='stockNow',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
