# Generated by Django 3.1 on 2022-04-30 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0016_auto_20220409_1033'),
        ('agency', '0046_auto_20220430_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailysubmission',
            name='categories',
            field=models.ManyToManyField(null=True, related_name='DailySubmission_categories_id', to='agency.CandidateCategories'),
        ),
        migrations.AlterField(
            model_name='dailysubmission',
            name='current_city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DailySubmission_current_city', to='candidate.city'),
        ),
        migrations.AlterField(
            model_name='dailysubmission',
            name='notice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DailySubmission_applyjob_notice_period', to='candidate.noticeperiod'),
        ),
        migrations.AlterField(
            model_name='dailysubmission',
            name='prefered_city',
            field=models.ManyToManyField(null=True, related_name='DailySubmission_prefered_city', to='candidate.City'),
        ),
        migrations.AlterField(
            model_name='dailysubmission',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='', verbose_name='DailySubmission_pf_pic'),
        ),
        migrations.AlterField(
            model_name='dailysubmission',
            name='skills',
            field=models.ManyToManyField(null=True, related_name='DailySubmission_skill_id', to='candidate.Skill'),
        ),
        migrations.AlterField(
            model_name='dailysubmission',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DailySubmission_source', to='candidate.source'),
        ),
        migrations.AlterField(
            model_name='dailysubmission',
            name='tags',
            field=models.ManyToManyField(null=True, related_name='DailySubmission_tags_id', to='agency.Tags'),
        ),
    ]
