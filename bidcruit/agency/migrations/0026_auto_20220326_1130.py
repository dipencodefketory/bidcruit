# Generated by Django 3.1 on 2022-03-26 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0005_stage_list_display_name'),
        ('agency', '0025_jobcreationtemplate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobcreationtemplate',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agencyjob_template_status_id', to='candidate.jobstatus'),
        ),
    ]
