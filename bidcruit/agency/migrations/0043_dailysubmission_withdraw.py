# Generated by Django 3.1 on 2022-04-23 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0042_dailysubmission_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailysubmission',
            name='withdraw',
            field=models.BooleanField(default=False),
        ),
    ]