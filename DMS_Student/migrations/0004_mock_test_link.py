# Generated by Django 3.2.4 on 2021-06-14 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMS_Student', '0003_rename_perk_job_perks'),
    ]

    operations = [
        migrations.AddField(
            model_name='mock_test',
            name='link',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
