# Generated by Django 2.0.7 on 2019-07-03 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20190702_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='o_modifyopinion',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proofing_progress.ModifyOpinion', verbose_name='打样修改意见'),
        ),
    ]
