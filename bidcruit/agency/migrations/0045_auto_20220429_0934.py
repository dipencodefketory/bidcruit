# Generated by Django 3.1 on 2022-04-29 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0044_auto_20220429_0806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailysubmission',
            name='candidate_custom_id',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='ctc',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='current_city',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='email',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='expectedctc',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='notice',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='prefered_city',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='secure_resume',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='secure_resume_file',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='source',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='total_exper',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='update_at',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='varify',
        ),
        migrations.RemoveField(
            model_name='dailysubmission',
            name='verified',
        ),
    ]