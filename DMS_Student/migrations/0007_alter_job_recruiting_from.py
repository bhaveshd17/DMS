# Generated by Django 3.2.5 on 2021-08-15 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMS_Student', '0006_auto_20210815_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='recruiting_from',
            field=models.CharField(default='NA', max_length=500, null=True),
        ),
    ]
