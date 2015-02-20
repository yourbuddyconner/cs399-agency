# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150219_0530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interesteduser',
            name='twitter_handle',
            field=models.CharField(max_length=100, null=True, validators=[django.core.validators.RegexValidator(regex=b'@([A-Za-z0-9_]+)', message=b'Please enter a valid twitter handle.')]),
            preserve_default=True,
        ),
    ]
