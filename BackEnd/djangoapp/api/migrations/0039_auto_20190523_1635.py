# Generated by Django 2.0.7 on 2019-05-23 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_naphtha_plan_all_months_naphtha_plan_single_month_naphtha_plan_summary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new_naphtha',
            name='new_Naphtha_Summary',
        ),
        migrations.RemoveField(
            model_name='new_naphtha_quality_lab',
            name='new_Naphtha',
        ),
        migrations.RemoveField(
            model_name='new_naphtha_quality_supplier',
            name='new_Naphtha',
        ),
        migrations.RemoveField(
            model_name='new_naphtha_summary',
            name='tanks_Overall_Status',
        ),
        migrations.RemoveField(
            model_name='receipt_tank',
            name='new_Naphtha',
        ),
        migrations.DeleteModel(
            name='New_Naphtha',
        ),
        migrations.DeleteModel(
            name='New_Naphtha_Quality_Lab',
        ),
        migrations.DeleteModel(
            name='New_Naphtha_Quality_Supplier',
        ),
        migrations.DeleteModel(
            name='New_Naphtha_Summary',
        ),
        migrations.DeleteModel(
            name='Receipt_Tank',
        ),
    ]
