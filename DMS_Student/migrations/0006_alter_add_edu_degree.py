# Generated by Django 3.2.4 on 2021-07-01 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMS_Student', '0005_alter_add_edu_degree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_edu',
            name='degree',
            field=models.CharField(max_length=50),
        ),
    ]