# Generated by Django 3.1 on 2022-03-28 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agency', '0029_agencyassignjob_assigninternal'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobWorkflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onthego', models.BooleanField(default=False)),
                ('withworkflow', models.BooleanField(default=False)),
                ('is_application_review', models.BooleanField(default=False)),
                ('agency_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_company_id_JobWorkflow', to='agency.agency')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agency_job_workflow_id', to='agency.jobcreation')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_create_user_id_JobWorkflow', to=settings.AUTH_USER_MODEL)),
                ('workflow_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_job_workflow_id', to='agency.workflows')),
            ],
        ),
    ]