# Generated by Django 4.0.4 on 2022-05-31 13:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_production_date',
            field=models.DateField(default=datetime.datetime(2022, 5, 31, 13, 9, 44, 709745, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_warranty_date',
            field=models.DateField(default=datetime.datetime(2022, 5, 31, 13, 9, 44, 709745, tzinfo=utc)),
        ),
    ]