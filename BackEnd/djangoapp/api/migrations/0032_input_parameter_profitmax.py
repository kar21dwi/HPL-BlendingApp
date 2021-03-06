# Generated by Django 2.0.7 on 2019-05-23 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_auto_20190523_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Input_Parameter_ProfitMax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Suction_Tank_No_PM', models.IntegerField()),
                ('Blending_Tank_No_PM', models.IntegerField()),
                ('Blend_Ratio_PM', models.FloatField()),
                ('Naphtha_Load_PM', models.FloatField()),
                ('LPG_Load_PM', models.FloatField()),
                ('C5_Load_PM', models.FloatField()),
                ('C6_Load_PM', models.FloatField()),
                ('Naphtha_Heater_PM', models.IntegerField()),
                ('COT_PM', models.FloatField()),
                ('GF_PDI_PM', models.FloatField()),
                ('Suc_Pressure_PM', models.FloatField()),
                ('Paraffin_PM', models.FloatField()),
                ('Olefins_PM', models.FloatField()),
                ('Aromatics_PM', models.FloatField()),
                ('Naphthene_PM', models.FloatField()),
                ('IN_IP_Ratio_PM', models.FloatField()),
                ('Density_PM', models.FloatField()),
                ('IBP_PM', models.FloatField(blank=True, null=True)),
                ('FBP_PM', models.FloatField(blank=True, null=True)),
                ('tanks_Overall_Status', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Tanks_Overall_Status')),
            ],
        ),
    ]
