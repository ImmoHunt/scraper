# Generated by Django 2.2.17 on 2021-08-30 19:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0081_auto_20210830_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 30, 19, 22, 43, 553546), verbose_name='comment date'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 30, 19, 22, 43, 552241), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 30, 19, 22, 43, 550758), verbose_name='date published'),
        ),
    ]
