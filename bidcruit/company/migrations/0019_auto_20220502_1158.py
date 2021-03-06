# Generated by Django 3.1 on 2022-05-02 11:58

import company.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0018_dailysubmission_candidate_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailysubmission',
            old_name='internal_candidate_id',
            new_name='internal_candidate_id_agency',
        ),
        migrations.AddField(
            model_name='dailysubmission',
            name='internal_candidate_id_company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='daily_submissionJob_id_company', to='company.internalcandidatebasicdetails'),
        ),
        migrations.AddField(
            model_name='dailysubmission',
            name='secure_resume',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='dailysubmission',
            name='secure_resume_file',
            field=models.FileField(max_length=500, null=True, upload_to=company.models.resume_path_handler),
        ),
    ]
