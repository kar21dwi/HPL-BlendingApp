# Generated by Django 2.0.7 on 2019-05-20 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20190520_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Level', models.FloatField(max_length=10)),
                ('Weight', models.FloatField(max_length=10)),
                ('Date_Time_Tank', models.FloatField()),
                ('quality_Avg', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Quality_Avg')),
                ('quality_Real', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Quality_Real')),
            ],
        ),
    ]
