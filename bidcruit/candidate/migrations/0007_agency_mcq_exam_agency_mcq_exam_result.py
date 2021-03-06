# Generated by Django 3.1 on 2022-03-31 10:27

import candidate.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agency', '0037_customresult_customscorecardresult'),
        ('candidate', '0006_agency_prerequisitesfill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency_Mcq_Exam_result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_question', models.IntegerField(null=True)),
                ('answered', models.IntegerField(null=True)),
                ('not_answered', models.IntegerField(null=True)),
                ('obain_time', models.CharField(max_length=10, null=True)),
                ('obain_marks', models.CharField(max_length=10, null=True)),
                ('mcq_pdf', models.FileField(max_length=500, null=True, upload_to=candidate.models.agency_mcqs_document_path_handler)),
                ('agency_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_mcq_exam_result', to='agency.agency')),
                ('candidate_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_candidate_mcq_exam_result', to=settings.AUTH_USER_MODEL)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agency_candidate_mcq_exam_job_id_result', to='agency.jobcreation')),
                ('template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_candidate_mcq_exam_template_id_result', to='agency.template_creation')),
            ],
        ),
        migrations.CreateModel(
            name='Agency_Mcq_Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('status', models.IntegerField(default=0, null=True)),
                ('time', models.CharField(max_length=100, null=True)),
                ('agency_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_company_mcq_exam', to='agency.agency')),
                ('candidate_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_candidate_mcq_exam', to=settings.AUTH_USER_MODEL)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agency_candidate_mcq_exam_job_id', to='agency.jobcreation')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_candidate_mcq_question', to='agency.mcq_question')),
                ('template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_candidate_mcq_exam_template_id', to='agency.template_creation')),
            ],
        ),
    ]
