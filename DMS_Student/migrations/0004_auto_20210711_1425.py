# Generated by Django 3.2.4 on 2021-07-11 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMS_Student', '0003_auto_20210711_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_email_verified',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='add_edu',
            name='diploma_pattern',
            field=models.CharField(choices=[('semester pattern', 'semester pattern'), ('NA', 'NA'), ('yearly pattern', 'yearly pattern')], default='NA', max_length=20),
        ),
    ]
