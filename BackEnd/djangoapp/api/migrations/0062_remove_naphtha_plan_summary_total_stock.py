# Generated by Django 2.0.7 on 2019-05-30 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0061_auto_20190530_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='naphtha_plan_summary',
            name='Total_Stock',
        ),
    ]