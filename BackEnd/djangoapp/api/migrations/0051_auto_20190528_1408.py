# Generated by Django 2.0.7 on 2019-05-28 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0050_auto_20190527_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quality_nir_pred',
            name='tanks_Overall_Status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Tanks_Overall_Status'),
        ),
    ]
