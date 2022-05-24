# Generated by Django 3.1 on 2022-04-06 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agency', '0037_customresult_customscorecardresult'),
        ('candidate', '0010_auto_20220405_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyRandomMCQExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_RandomMCQExam_exam', to='agency.agency')),
                ('candidate_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_candidate_RandomMCQExam_exam', to=settings.AUTH_USER_MODEL)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agency_RandomMCQExam_exam_job_id', to='agency.jobcreation')),
                ('question', models.ManyToManyField(null=True, related_name='agency_RandomMCQExam_question', to='agency.mcq_Question')),
                ('template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_RandomMCQExam_exam_template_id', to='agency.template_creation')),
            ],
        ),
        migrations.CreateModel(
            name='AgencyRandomImageExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_RandomImageExam_exam', to='agency.agency')),
                ('candidate_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_candidate_RandomImageExam_exam', to=settings.AUTH_USER_MODEL)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agency_candidate_RandomImageExam_exam_job_id', to='agency.jobcreation')),
                ('question', models.ManyToManyField(null=True, related_name='agency_candidate_RandomImageExam_question', to='agency.ImageQuestion')),
                ('template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_candidate_RandomImageExam_exam_template_id', to='agency.template_creation')),
            ],
        ),
    ]