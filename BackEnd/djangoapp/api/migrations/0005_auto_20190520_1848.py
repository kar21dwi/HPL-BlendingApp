# Generated by Django 2.0.7 on 2019-05-20 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_quality_avg_quality_real_tank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tank',
            name='quality_Avg',
        ),
        migrations.RemoveField(
            model_name='tank',
            name='quality_Real',
        ),
        migrations.DeleteModel(
            name='Tank',
        ),
    ]
