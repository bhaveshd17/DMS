# Generated by Django 3.2.4 on 2021-06-13 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DMS_Student', '0002_rename_skill_job_skills'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='perk',
            new_name='perks',
        ),
    ]
