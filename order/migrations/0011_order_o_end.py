# Generated by Django 2.0.7 on 2019-07-04 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_order_o_accountingdocuments'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='o_end',
            field=models.BooleanField(default=False, verbose_name='订单是否完成/默认未完成'),
        ),
    ]
