# Generated by Django 2.0.7 on 2019-05-17 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proofing_progress', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proofingprogress',
            name='pp_Modify_sample_arrival_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='到料时间（修改）'),
        ),
        migrations.AlterField(
            model_name='proofingprogress',
            name='pp_Modify_sample_express_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='快递时间（修改）'),
        ),
        migrations.AlterField(
            model_name='proofingprogress',
            name='pp_Modify_sample_order_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='下单时间（修改）'),
        ),
        migrations.AlterField(
            model_name='proofingprogress',
            name='pp_corrective_information',
            field=models.TextField(blank=True, null=True, verbose_name='整改信息'),
        ),
        migrations.AlterField(
            model_name='proofingprogress',
            name='pp_customer_feedback',
            field=models.TextField(blank=True, null=True, verbose_name='客人反馈信息'),
        ),
        migrations.AlterField(
            model_name='proofingprogress',
            name='pp_sample_arrival_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='到料时间'),
        ),
        migrations.AlterField(
            model_name='proofingprogress',
            name='pp_sample_express_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='快递时间'),
        ),
        migrations.AlterField(
            model_name='proofingprogress',
            name='pp_sample_order_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='下单时间'),
        ),
    ]