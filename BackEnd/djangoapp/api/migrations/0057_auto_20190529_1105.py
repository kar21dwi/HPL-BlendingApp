# Generated by Django 2.0.7 on 2019-05-29 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0056_login_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='input_parameter_userdefined',
            name='quality_Real',
        ),
        migrations.AddField(
            model_name='input_parameter_userdefined',
            name='tanks_Overall_Status',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Tanks_Overall_Status'),
        ),
    ]
