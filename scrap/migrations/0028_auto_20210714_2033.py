# Generated by Django 2.2.17 on 2021-07-14 20:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0027_auto_20210714_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 14, 20, 33, 55, 152728), verbose_name='comment date'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 14, 20, 33, 55, 151266), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 14, 20, 33, 55, 149607), verbose_name='date published'),
        ),
    ]
