# Generated by Django 3.1 on 2022-03-04 05:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agency', '0002_auto_20220303_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('agency_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tags_agency', to='agency.agency')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agency_Tags_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='internalcandidatebasicdetail',
            name='tags',
            field=models.ManyToManyField(null=True, related_name='InternalCandidateBasicDetail_tags_id', to='agency.Tags'),
        ),
    ]
