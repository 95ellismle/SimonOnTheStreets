# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-28 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnTheGo', '0005_serviceuser_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceuser',
            name='total_goals',
            field=models.IntegerField(default=10, verbose_name=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='serviceuser',
            name='age',
            field=models.IntegerField(verbose_name=22),
        ),
    ]
