# Generated by Django 3.2.4 on 2021-07-05 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMS_Student', '0018_auto_20210705_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_edu',
            name='degree',
            field=models.CharField(choices=[('12', '12th'), ('10', '10th'), ('diploma', 'Diploma')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='drop',
            field=models.CharField(choices=[('Greater than 2', 3), ('0', 0), ('1', 1), ('2', 2)], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='live_kt',
            field=models.CharField(choices=[('0', 0), ('5', 5), ('6', 6), ('Greater than 6', 7), ('2', 2), ('4', 4), ('3', 3), ('1', 1)], max_length=15, null=True),
        ),
    ]
