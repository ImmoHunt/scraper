# Generated by Django 2.2.17 on 2021-08-24 18:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0071_auto_20210824_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 24, 18, 0, 54, 766337), verbose_name='comment date'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 24, 18, 0, 54, 764915), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 24, 18, 0, 54, 763281), verbose_name='date published'),
        ),
    ]
