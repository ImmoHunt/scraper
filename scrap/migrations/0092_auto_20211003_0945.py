# Generated by Django 2.2.17 on 2021-10-03 09:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0091_auto_20210918_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 3, 9, 45, 52, 772507), verbose_name='comment date'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 3, 9, 45, 52, 770612), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 3, 9, 45, 52, 768549), verbose_name='date published'),
        ),
    ]
