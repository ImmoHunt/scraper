# Generated by Django 2.2.17 on 2021-01-18 21:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0005_auto_20210117_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 18, 21, 4, 38, 828986), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 18, 21, 4, 38, 827145), verbose_name='date published'),
        ),
    ]
