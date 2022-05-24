# Generated by Django 3.1 on 2022-03-29 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_candidatejobstagesstatus_custom_stage_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customresult',
            name='enable_file_input',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customresult',
            name='enable_response',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customresult',
            name='file_input',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='customresult',
            name='title',
            field=models.CharField(max_length=500, null=True),
        ),
    ]