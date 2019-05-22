# Generated by Django 2.0.7 on 2019-05-22 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20190522_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant_Constraints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Max_Ethylene', models.FloatField()),
                ('Max_Propylene', models.FloatField()),
                ('Max_RPG', models.FloatField()),
                ('Max_C4_Mix', models.FloatField()),
                ('Max_Fuel_Gas', models.FloatField()),
                ('Max_Benzene', models.FloatField()),
                ('Max_BD', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Quality_Avg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Paraffin', models.FloatField(max_length=10)),
                ('Olefins', models.FloatField(max_length=10)),
                ('Aromatics', models.FloatField(max_length=10)),
                ('Naphthene', models.FloatField()),
                ('IN_IP_Ratio', models.FloatField()),
                ('Density', models.FloatField()),
                ('IBP', models.FloatField(null=True)),
                ('FBP', models.FloatField(null=True)),
                ('Sulfur', models.FloatField(null=True)),
                ('Colour', models.CharField(max_length=50, null=True)),
                ('RVP', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quality_NIR_Actual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Paraffin_NIR', models.FloatField()),
                ('Aromatics_NIR', models.FloatField()),
                ('Density_NIR', models.FloatField()),
                ('IN_IP_Ratio_NIR', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Quality_NIR_Pred',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Paraffin_NIR_Pred', models.FloatField()),
                ('Aromatics_NIR_Pred', models.FloatField()),
                ('Density_NIR_Pred', models.FloatField()),
                ('IN_IP_Ratio_NIR_Pred', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Quality_Real',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Paraffin_Real', models.FloatField()),
                ('Aromatics_Real', models.FloatField()),
                ('Density_Real', models.FloatField()),
                ('IN_IP_Ratio_Real', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='tank',
            name='Level',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tank',
            name='Tank_No',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tank',
            name='Weight',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tanks_overall_status',
            name='Blend_Ratio_RN',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tanks_overall_status',
            name='Blending_Tank_No_RN',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tanks_overall_status',
            name='Suction_Tank_No_RN',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='quality_real',
            name='tank',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Tank'),
        ),
        migrations.AddField(
            model_name='quality_nir_pred',
            name='tanks_Overall_Status',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Tanks_Overall_Status'),
        ),
        migrations.AddField(
            model_name='quality_nir_actual',
            name='tanks_Overall_Status',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Tanks_Overall_Status'),
        ),
        migrations.AddField(
            model_name='quality_avg',
            name='tank',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Tank'),
        ),
        migrations.AddField(
            model_name='plant_constraints',
            name='tanks_Overall_Status',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Tanks_Overall_Status'),
        ),
    ]
