# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockScreener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='ma20',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='ma5',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='ma60',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
