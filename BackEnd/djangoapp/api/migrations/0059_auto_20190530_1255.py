# Generated by Django 2.0.7 on 2019-05-30 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0058_auto_20190529_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='output_comparision',
            name='IN_IP_Ratio',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
