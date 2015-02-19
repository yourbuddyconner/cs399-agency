# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_campaign_formid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interesteduser',
            name='address_city',
        ),
        migrations.RemoveField(
            model_name='interesteduser',
            name='address_state',
        ),
        migrations.RemoveField(
            model_name='interesteduser',
            name='address_street',
        ),
        migrations.RemoveField(
            model_name='interesteduser',
            name='address_zip',
        ),
        migrations.AddField(
            model_name='interesteduser',
            name='twitter_handle',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
