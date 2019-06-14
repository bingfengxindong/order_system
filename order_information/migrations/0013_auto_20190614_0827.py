# Generated by Django 2.0.7 on 2019-06-14 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order_information', '0012_auto_20190611_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pt_id', models.UUIDField(verbose_name='编号')),
                ('pt_type', models.CharField(max_length=20, verbose_name='币种')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('create_end_date', models.DateTimeField(auto_now=True)),
                ('isdelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '币种',
                'verbose_name_plural': '币种',
                'ordering': ['pk'],
            },
        ),
        migrations.RemoveField(
            model_name='productinfo',
            name='pi_price_type',
        ),
        migrations.AddField(
            model_name='order',
            name='o_price_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order_information.PriceType', verbose_name='币种'),
        ),
    ]