# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-26 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('S', 'In Store'), ('O', 'Online'), ('X', 'Other')], max_length=1),
        ),
    ]
