# Generated by Django 2.0.7 on 2019-05-22 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20190522_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tank',
            name='tanks_Overall_Status',
        ),
        migrations.DeleteModel(
            name='Tank',
        ),
        migrations.DeleteModel(
            name='Tanks_Overall_Status',
        ),
    ]
