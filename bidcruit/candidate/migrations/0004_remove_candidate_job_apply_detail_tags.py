# Generated by Django 3.1 on 2022-03-04 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0003_permissionsmodel_display_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate_job_apply_detail',
            name='tags',
        ),
    ]