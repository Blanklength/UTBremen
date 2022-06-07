# Generated by Django 4.0.5 on 2022-06-07 20:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0003_alter_device_device_production_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_production_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 7, 20, 35, 1, 243739, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_warranty_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 7, 20, 35, 1, 243739, tzinfo=utc)),
        ),
    ]
