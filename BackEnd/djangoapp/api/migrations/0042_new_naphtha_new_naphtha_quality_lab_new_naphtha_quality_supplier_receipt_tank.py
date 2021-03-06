# Generated by Django 2.0.7 on 2019-05-23 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0041_auto_20190523_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='New_Naphtha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Transport_Type', models.CharField(max_length=50)),
                ('Date_Transfer_From', models.DateField()),
                ('Date_Transfer_To', models.DateField()),
                ('HOJ', models.IntegerField()),
                ('Load_Port', models.CharField(max_length=50)),
                ('BL_Quantity', models.FloatField()),
                ('Shore_Quantity', models.FloatField()),
                ('Opening_Stock', models.IntegerField(blank=True, null=True)),
                ('Source', models.CharField(max_length=50)),
                ('PCN_NCU', models.IntegerField(blank=True, null=True)),
                ('PCN_CPP', models.IntegerField(blank=True, null=True)),
                ('FGN_CPP', models.IntegerField(blank=True, null=True)),
                ('CBFS_CPP', models.IntegerField(blank=True, null=True)),
                ('Vessel_Name', models.CharField(max_length=50)),
                ('Shortage_Quantity', models.FloatField(blank=True, null=True)),
                ('tanks_Overall_Status', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Tanks_Overall_Status')),
            ],
        ),
        migrations.CreateModel(
            name='New_Naphtha_Quality_Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Paraffin', models.FloatField()),
                ('Olefins', models.FloatField()),
                ('Aromatics', models.FloatField()),
                ('Naphthene', models.FloatField()),
                ('IN_IP_Ratio', models.FloatField()),
                ('Density', models.FloatField()),
                ('IBP', models.FloatField(blank=True, null=True)),
                ('FBP', models.FloatField(blank=True, null=True)),
                ('Sulfur', models.FloatField(blank=True, null=True)),
                ('Colour', models.FloatField()),
                ('RVP', models.FloatField(blank=True, null=True)),
                ('new_Naphtha', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.New_Naphtha')),
            ],
        ),
        migrations.CreateModel(
            name='New_Naphtha_Quality_Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Paraffin', models.FloatField(blank=True, null=True)),
                ('Olefins', models.FloatField(blank=True, null=True)),
                ('Aromatics', models.FloatField(blank=True, null=True)),
                ('Naphthene', models.FloatField(blank=True, null=True)),
                ('IN_IP_Ratio', models.FloatField(blank=True, null=True)),
                ('Density', models.FloatField(blank=True, null=True)),
                ('IBP', models.FloatField(blank=True, null=True)),
                ('FBP', models.FloatField(blank=True, null=True)),
                ('Sulfur', models.FloatField(blank=True, null=True)),
                ('Colour', models.FloatField(blank=True, null=True)),
                ('RVP', models.FloatField(blank=True, null=True)),
                ('new_Naphtha', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.New_Naphtha')),
            ],
        ),
        migrations.CreateModel(
            name='Receipt_Tank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tank_No_1', models.FloatField(default=0)),
                ('Tank_No_2', models.FloatField(default=0)),
                ('Tank_No_3', models.FloatField(default=0)),
                ('Tank_No_4', models.FloatField(default=0)),
                ('Tank_No_5', models.FloatField(default=0)),
                ('new_Naphtha', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.New_Naphtha')),
            ],
        ),
    ]
