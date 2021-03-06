# Generated by Django 2.0.7 on 2019-07-02 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModifyOpinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mo_id', models.UUIDField(verbose_name='编号')),
                ('mo_customer_info', models.TextField(blank=True, null=True, verbose_name='客人反馈信息')),
                ('mo_factory_info', models.TextField(blank=True, null=True, verbose_name='工厂修改信息')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('create_end_date', models.DateTimeField(auto_now=True)),
                ('isdelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '打样修改意见表',
                'verbose_name_plural': '打样修改意见表',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='ProofingProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pp_id', models.UUIDField(verbose_name='编号')),
                ('pp_number', models.CharField(blank=True, max_length=200, null=True, verbose_name='样品单号')),
                ('pp_erp_number', models.CharField(blank=True, max_length=200, null=True, verbose_name='ERP单号')),
                ('pp_date', models.DateField(blank=True, null=True, verbose_name='接单时间')),
                ('pp_delivery_date', models.DateField(blank=True, null=True, verbose_name='交货日期')),
                ('pp_main_fabric_arrival', models.DateField(blank=True, null=True, verbose_name='主料到货')),
                ('pp_ingredients_fabric_arrival', models.DateField(blank=True, null=True, verbose_name='辅料到货')),
                ('pp_tailor_date', models.DateField(blank=True, null=True, verbose_name='裁剪日期')),
                ('pp_send_embroide', models.DateField(blank=True, null=True, verbose_name='送绣花')),
                ('pp_receive_embroide', models.DateField(blank=True, null=True, verbose_name='绣花回')),
                ('pp_send_print', models.DateField(blank=True, null=True, verbose_name='送印花')),
                ('pp_receive_print', models.DateField(blank=True, null=True, verbose_name='印花回')),
                ('pp_delivery_proofing', models.DateField(blank=True, null=True, verbose_name='发样品')),
                ('pp_end_date', models.DateField(blank=True, null=True, verbose_name='完成日期')),
                ('pp_express_date', models.DateField(blank=True, null=True, verbose_name='快递时间')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('create_end_date', models.DateTimeField(auto_now=True)),
                ('isdelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '打样表',
                'verbose_name_plural': '打样表',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w_id', models.UUIDField(verbose_name='编号')),
                ('w_worker', models.CharField(blank=True, max_length=200, null=True, verbose_name='操作工')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('create_end_date', models.DateTimeField(auto_now=True)),
                ('isdelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '操作工表',
                'verbose_name_plural': '操作工表',
                'ordering': ['pk'],
            },
        ),
        migrations.AddField(
            model_name='proofingprogress',
            name='pp_worker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proofing_progress.Worker', verbose_name='操作工'),
        ),
    ]
