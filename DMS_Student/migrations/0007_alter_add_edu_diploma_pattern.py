# Generated by Django 3.2.5 on 2021-12-07 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMS_Student', '0006_auto_20211001_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_edu',
            name='diploma_pattern',
            field=models.CharField(choices=[('yearly pattern', 'yearly pattern'), ('semester pattern', 'semester pattern'), ('NA', 'NA')], default='NA', max_length=20),
        ),
    ]