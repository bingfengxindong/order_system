# Generated by Django 2.0.7 on 2019-05-16 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ps_id', models.UUIDField(verbose_name='编号')),
                ('ps_order_date', models.DateField(verbose_name='下单时间')),
                ('ps_arrival_date', models.DateField(verbose_name='倒料时间')),
                ('ps_tailor_date', models.DateField(verbose_name='裁剪时间')),
                ('ps_embroider_date', models.DateField(verbose_name='绣花时间')),
                ('ps_print_date', models.DateField(verbose_name='印花时间')),
                ('ps_Water_washing_date', models.DateField(verbose_name='水洗时间')),
                ('ps_sewing_date', models.DateField(verbose_name='车缝时间')),
                ('ps_qc_date', models.DateField(verbose_name='QC时间')),
                ('ps_outward_transport_date', models.DateField(verbose_name='外运时间')),
                ('ps_gathering_date', models.DateField(verbose_name='收款时间')),
                ('ps_price_type', models.CharField(max_length=50, verbose_name='金额类型')),
                ('ps_gathering_price', models.CharField(max_length=100, verbose_name='收款金额')),
                ('ps_contract_balance', models.CharField(max_length=100, verbose_name='合同余额')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('create_end_date', models.DateTimeField(auto_now=True)),
                ('isdelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '大货进度表',
                'verbose_name_plural': '大货进度表',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='ProductionWorkshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pw_id', models.UUIDField(verbose_name='编号')),
                ('pw_workshop', models.CharField(max_length=200, verbose_name='生产车间')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('create_end_date', models.DateTimeField(auto_now=True)),
                ('isdelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '生产车间',
                'verbose_name_plural': '生产车间',
                'ordering': ['pk'],
            },
        ),
        migrations.AddField(
            model_name='productionschedule',
            name='ps_workshop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production_schedule.ProductionWorkshop', verbose_name='生产车间'),
        ),
    ]