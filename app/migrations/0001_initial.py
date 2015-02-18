# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('instructions', models.TextField()),
                ('start_date', models.DateField(verbose_name=b'day the campaign begins')),
                ('end_date', models.DateField(verbose_name=b'day the campaign ends')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InterestedUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('address_street', models.CharField(max_length=150)),
                ('address_city', models.CharField(max_length=150)),
                ('address_state', models.CharField(max_length=150)),
                ('address_zip', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
