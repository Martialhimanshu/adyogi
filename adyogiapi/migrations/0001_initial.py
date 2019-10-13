# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, null=True, blank=True)),
                ('is_active', models.BooleanField(default=False)),
                ('slug', models.CharField(max_length=32, null=True, blank=True)),
                ('product_type', models.IntegerField(default=0, null=True, blank=True, choices=[(1, b'Development'), (2, b'Production')])),
            ],
        ),
    ]
