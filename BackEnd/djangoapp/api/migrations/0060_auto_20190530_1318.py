# Generated by Django 2.0.7 on 2019-05-30 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0059_auto_20190530_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='naphtha_plan_single_month',
            name='Actual_NCU_TPD',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='naphtha_plan_single_month',
            name='Budget_NCU_TPD',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='naphtha_plan_single_month',
            name='Actual_CPP_TPD',
            field=models.IntegerField(default=228),
        ),
        migrations.AlterField(
            model_name='naphtha_plan_single_month',
            name='Actual_NCU_TPH',
            field=models.IntegerField(default=238),
        ),
        migrations.AlterField(
            model_name='naphtha_plan_single_month',
            name='Budget_CPP_TPD',
            field=models.IntegerField(default=228),
        ),
        migrations.AlterField(
            model_name='naphtha_plan_single_month',
            name='Budget_NCU_TPH',
            field=models.IntegerField(default=238),
        ),
    ]
