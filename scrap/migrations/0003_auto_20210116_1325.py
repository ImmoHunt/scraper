# Generated by Django 2.2.17 on 2021-01-16 13:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0002_auto_20210116_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_photo',
            field=models.ImageField(default='default.jpg', upload_to='photos/', verbose_name='Minha foto'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 16, 13, 25, 38, 246704), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 16, 13, 25, 38, 245132), verbose_name='date published'),
        ),
    ]
