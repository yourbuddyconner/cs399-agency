# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150219_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='interesteduser',
            name='dog_preferance',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
