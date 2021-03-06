# Generated by Django 3.1 on 2022-05-02 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0047_auto_20220430_1324'),
        ('company', '0015_dailysubmission'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailysubmission',
            old_name='internal_user',
            new_name='internal_user_company',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='secure_resume',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='secure_resume_file',
        ),
        migrations.AddField(
            model_name='dailysubmission',
            name='agency_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='daily_submission_AssociateJob_agency_company', to='agency.agency'),
        ),
        migrations.DeleteModel(
            name='AppliedCandidateBasicDetails',
        ),
    ]
