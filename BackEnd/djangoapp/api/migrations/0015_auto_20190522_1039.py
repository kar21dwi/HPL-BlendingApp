# Generated by Django 2.0.7 on 2019-05-22 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_tank'),
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
            name='Quality_Avg',
        ),
        migrations.DeleteModel(
            name='Quality_Real',
        ),
        migrations.DeleteModel(
            name='Tank',
        ),
    ]
