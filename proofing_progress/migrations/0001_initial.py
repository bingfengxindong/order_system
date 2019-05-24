# Generated by Django 2.0.7 on 2019-05-16 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProofingProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pp_id', models.UUIDField(verbose_name='编号')),
                ('pp_sample_order_date', models.DateField(verbose_name='下单时间')),
                ('pp_sample_arrival_date', models.DateField(verbose_name='到料时间')),
                ('pp_sample_express_date', models.DateField(verbose_name='快递时间')),
                ('pp_customer_feedback', models.TextField(verbose_name='客人反馈信息')),
                ('pp_corrective_information', models.TextField(verbose_name='整改信息')),
                ('pp_Modify_sample_order_date', models.DateField(verbose_name='下单时间（修改）')),
                ('pp_Modify_sample_arrival_date', models.DateField(verbose_name='到料时间（修改）')),
                ('pp_Modify_sample_express_date', models.DateField(verbose_name='快递时间（修改）')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('create_end_date', models.DateTimeField(auto_now=True)),
                ('isdelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '打样进度表',
                'verbose_name_plural': '打样进度表',
                'ordering': ['pk'],
            },
        ),
    ]