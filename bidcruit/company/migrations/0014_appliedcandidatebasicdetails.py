# Generated by Django 3.1 on 2022-04-30 13:24

import company.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0016_auto_20220409_1033'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0013_auto_20220423_0758'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppliedCandidateBasicDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_custom_id', models.CharField(max_length=10, null=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=100)),
                ('resume', models.FileField(max_length=500, null=True, upload_to=company.models.resume_path_handler)),
                ('secure_resume', models.BooleanField(default=False)),
                ('secure_resume_file', models.FileField(max_length=500, null=True, upload_to=company.models.resume_path_handler)),
                ('contact', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=100)),
                ('ctc', models.CharField(max_length=100, null=True)),
                ('expectedctc', models.CharField(max_length=100, null=True)),
                ('total_exper', models.CharField(max_length=100, null=True)),
                ('profile_pic', models.ImageField(null=True, upload_to='', verbose_name='AppliedCandidateBasicDetails_pf_pic')),
                ('create_at', models.DateTimeField(auto_now_add=True, max_length=200)),
                ('update_at', models.DateTimeField(max_length=200, null=True)),
                ('candidate_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Candidateid_AppliedCandidateBasicDetails', to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(null=True, related_name='agency_add_AppliedCandidateBasicDetails_categories_id', to='company.CandidateCategories')),
                ('current_city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='AppliedCandidateBasicDetails_current_city', to='candidate.city')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AppliedCandidateBasicDetails_job', to='company.jobcreation')),
                ('notice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='AppliedCandidateBasicDetails_applyjob_notice_period', to='candidate.noticeperiod')),
                ('prefered_city', models.ManyToManyField(null=True, related_name='AppliedCandidateBasicDetails_prefered_city', to='candidate.City')),
                ('skills', models.ManyToManyField(null=True, related_name='AppliedCandidateBasicDetails_skill_id', to='candidate.Skill')),
                ('source', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='AppliedCandidateBasicDetails_source', to='candidate.source')),
                ('tags', models.ManyToManyField(null=True, related_name='AppliedCandidateBasicDetails_tags_id', to='company.Tags')),
            ],
        ),
    ]
