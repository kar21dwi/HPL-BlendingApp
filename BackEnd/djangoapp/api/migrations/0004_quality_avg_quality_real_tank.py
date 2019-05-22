# Generated by Django 2.0.7 on 2019-05-20 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_tank'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quality_Avg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Paraffin', models.FloatField(max_length=10)),
                ('Olefins', models.FloatField(max_length=10)),
                ('Aromatics', models.FloatField(max_length=10)),
                ('Napthene', models.FloatField(max_length=10)),
                ('IN_IP_Ratio', models.FloatField(max_length=10)),
                ('Density', models.FloatField(max_length=10)),
                ('IBP', models.FloatField(max_length=10)),
                ('FBP', models.FloatField(max_length=10)),
                ('Date_Time', models.DateTimeField()),
                ('Colour', models.CharField(blank=True, max_length=10, null=True)),
                ('RVP', models.FloatField(blank=True, max_length=10, null=True)),
                ('Sulfur', models.FloatField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quality_Real',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Paraffin_Real', models.FloatField(max_length=10)),
                ('Aromatics_Real', models.FloatField(max_length=10)),
                ('IN_IP_Ratio_Real', models.FloatField(max_length=10)),
                ('Density_Real', models.FloatField(max_length=10)),
                ('Date_Time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality_Avg', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='api.Quality_Avg')),
                ('quality_Real', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='api.Quality_Real')),
                ('Level', models.FloatField(max_length=10)),
                ('Weight', models.FloatField(max_length=10)),
                ('Date_Time', models.FloatField()),
            ],
        ),
    ]
