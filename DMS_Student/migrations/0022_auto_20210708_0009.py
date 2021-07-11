# Generated by Django 3.2.4 on 2021-07-07 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMS_Student', '0021_auto_20210708_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_edu',
            name='diploma_pattern',
            field=models.CharField(choices=[('semester pattern', 'semester pattern'), ('NA', 'NA'), ('yearly pattern', 'yearly pattern')], default='NA', max_length=20),
        ),
        migrations.AlterField(
            model_name='curredu',
            name='drop',
            field=models.CharField(choices=[('0', '0 year'), ('1', '1 year'), ('2', '2 years'), ('3', '3 years'), ('4', '4 years'), ('5', '5 years')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='drop',
            field=models.CharField(choices=[('3', 'Greater than 2'), ('0', '0'), ('2', '2'), ('1', '1')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='live_kt',
            field=models.CharField(choices=[('5', '5'), ('0', '0'), ('4', '4'), ('6', '6'), ('7', 'Greater than 6'), ('1', '1'), ('3', '3'), ('2', '2')], max_length=15, null=True),
        ),
    ]
