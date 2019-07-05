# Generated by Django 2.0.7 on 2019-07-04 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_id', models.UUIDField(verbose_name='编号')),
                ('q_offer', models.CharField(blank=True, max_length=200, null=True, verbose_name='大货单价')),
                ('q_floating_rate', models.CharField(blank=True, max_length=200, null=True, verbose_name='浮动率')),
                ('q_end_offer', models.CharField(blank=True, max_length=200, null=True, verbose_name='最终报价')),
                ('q_fabric_quotation', models.CharField(blank=True, max_length=200, null=True, verbose_name='面料报价')),
                ('q_ingredients_quotation', models.CharField(blank=True, max_length=200, null=True, verbose_name='辅料报价')),
                ('q_labor_payment_quotation', models.CharField(blank=True, max_length=200, null=True, verbose_name='工缴报价')),
                ('q_water_washing_quotation', models.CharField(blank=True, max_length=200, null=True, verbose_name='水洗报价')),
                ('q_embroider_quotation', models.CharField(blank=True, max_length=200, null=True, verbose_name='绣花报价')),
                ('q_print_quotation', models.CharField(blank=True, max_length=200, null=True, verbose_name='印花报价')),
                ('q_packaging_quotation', models.CharField(blank=True, max_length=200, null=True, verbose_name='包装物报价')),
                ('q_other_quotation', models.CharField(blank=True, max_length=200, null=True, verbose_name='其他报价')),
                ('q_reserved_profits', models.CharField(blank=True, max_length=200, null=True, verbose_name='预留利润')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('create_end_date', models.DateTimeField(auto_now=True)),
                ('isdelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '报价单表',
                'verbose_name_plural': '报价单表',
                'ordering': ['pk'],
            },
        ),
    ]