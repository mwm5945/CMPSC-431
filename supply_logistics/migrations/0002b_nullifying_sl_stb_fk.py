# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supply_logistics', '0002_auto_20160718_2256')
        # 0078 depends on this
    ]

    operations = [
        migrations.AlterField(
            model_name='SuppliesDonations',
            name='thankyou_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='SuppliesDonations',
            name='thankyou_captain',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='SuppliesDonations',
            name='did',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='SuppliesDonations',
            name='oid',
            field=models.IntegerField(null=True, blank=True),
        ),

    ]
