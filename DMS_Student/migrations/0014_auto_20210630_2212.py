# Generated by Django 3.2.4 on 2021-06-30 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMS_Student', '0013_auto_20210630_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='date',
        ),
        migrations.AddField(
            model_name='job_user',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]