# Generated by Django 3.1 on 2022-05-12 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0020_taststatus_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taststatus',
            name='color',
        ),
    ]
