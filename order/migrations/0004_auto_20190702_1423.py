# Generated by Django 2.0.7 on 2019-07-02 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proofing_progress', '0001_initial'),
        ('order', '0003_auto_20190702_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='o_modifyopinion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proofing_progress.ModifyOpinion', verbose_name='打样修改意见'),
        ),
        migrations.AddField(
            model_name='order',
            name='o_proofingprogress',
            field=models.ManyToManyField(blank=True, null=True, to='proofing_progress.ProofingProgress', verbose_name='打样'),
        ),
    ]
