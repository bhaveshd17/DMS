# Generated by Django 3.2.4 on 2021-07-08 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMS_Student', '0022_auto_20210708_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_edu',
            name='diploma_pattern',
            field=models.CharField(choices=[('yearly pattern', 'yearly pattern'), ('NA', 'NA'), ('semester pattern', 'semester pattern')], default='NA', max_length=20),
        ),
        migrations.AlterField(
            model_name='job',
            name='drop',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('3', 'Greater than 2'), ('2', '2')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='live_kt',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('5', '5'), ('7', 'Greater than 6'), ('4', '4'), ('3', '3'), ('6', '6'), ('2', '2')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=15, null=True),
        ),
    ]
