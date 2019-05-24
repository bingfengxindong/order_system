# Generated by Django 2.0.7 on 2019-05-18 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_information', '0004_auto_20190518_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='pi_amount',
            field=models.IntegerField(blank=True, null=True, verbose_name='下单数量'),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='pi_date',
            field=models.DateField(blank=True, null=True, verbose_name='交货日期'),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='pi_price_type',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='单价类型'),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='pi_unit_price',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='下单单价'),
        ),
    ]