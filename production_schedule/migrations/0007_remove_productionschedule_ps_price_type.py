# Generated by Django 2.0.7 on 2019-06-14 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('production_schedule', '0006_auto_20190611_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productionschedule',
            name='ps_price_type',
        ),
    ]
