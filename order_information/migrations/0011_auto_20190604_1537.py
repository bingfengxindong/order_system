# Generated by Django 2.0.7 on 2019-06-04 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proofing_progress', '0004_auto_20190603_1553'),
        ('order_information', '0010_auto_20190604_0839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='o_proofingprogress',
        ),
        migrations.AddField(
            model_name='order',
            name='o_proofingprogress',
            field=models.ManyToManyField(blank=True, null=True, to='proofing_progress.ProofingProgress', verbose_name='打样进度'),
        ),
    ]
