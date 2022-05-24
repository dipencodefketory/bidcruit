# Generated by Django 3.1 on 2022-03-26 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0005_stage_list_display_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agency', '0026_auto_20220326_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workflows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('is_configured', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(max_length=200, null=True)),
                ('delete_at', models.DateTimeField(max_length=200, null=True)),
                ('agency_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_id_Workflows', to='agency.agency')),
                ('delete_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_delete_user_id_Workflows', to=settings.AUTH_USER_MODEL)),
                ('update_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_update_user_id_Workflows', to=settings.AUTH_USER_MODEL)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_create_user_id_Workflows', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkflowStages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_name', models.CharField(max_length=100)),
                ('sequence_number', models.IntegerField()),
                ('display', models.BooleanField(default=True)),
                ('agency_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_id_WorkflowStages', to='agency.agency')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_workflow_category', to='agency.templatecategory')),
                ('stage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_workflow_stage', to='candidate.stage_list')),
                ('template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_workflow_template', to='agency.template_creation')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_create_user_id_WorkflowStages', to=settings.AUTH_USER_MODEL)),
                ('workflow', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_workflow_id', to='agency.workflows')),
            ],
        ),
        migrations.CreateModel(
            name='WorkflowConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_automation', models.BooleanField(null=True)),
                ('shortlist', models.FloatField(null=True)),
                ('onhold', models.FloatField(null=True)),
                ('reject', models.FloatField(null=True)),
                ('agency_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_id_WorkflowConfiguration', to='agency.agency')),
                ('interviewer', models.ManyToManyField(null=True, related_name='agency_interview_name', to=settings.AUTH_USER_MODEL)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_create_user_id_WorkflowConfiguration', to=settings.AUTH_USER_MODEL)),
                ('workflow_stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agency_workflow_stage_id', to='agency.workflowstages')),
            ],
        ),
    ]