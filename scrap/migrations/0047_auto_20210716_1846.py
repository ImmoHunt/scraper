# Generated by Django 2.2.17 on 2021-07-16 18:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0046_auto_20210716_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 16, 18, 46, 58, 225642), verbose_name='comment date'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 16, 18, 46, 58, 224204), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 16, 18, 46, 58, 222543), verbose_name='date published'),
        ),
    ]
