# Generated by Django 3.2.4 on 2021-07-07 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMS_Student', '0012_auto_20210707_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_edu',
            name='diploma_pattern',
            field=models.CharField(choices=[('NA', 'NA'), ('semester pattern', 'semester pattern'), ('yearly pattern', 'yearly pattern')], default='NA', max_length=20),
        ),
        migrations.AlterField(
            model_name='add_edu',
            name='gap',
            field=models.CharField(choices=[('0', '0 year'), ('1', '1 year'), ('2', '2 years'), ('3', '3 years'), ('4', '4 years'), ('5', '5 years')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='curredu',
            name='drop',
            field=models.CharField(choices=[('0', '0 year'), ('1', '1 year'), ('2', '2 years'), ('3', '3 years'), ('4', '4 years'), ('5', '5 years')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='drop',
            field=models.CharField(choices=[('1', '1'), ('0', '0'), ('3', 'Greater than 2'), ('2', '2')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='live_kt',
            field=models.CharField(choices=[('4', '4'), ('6', '6'), ('3', '3'), ('7', 'Greater than 6'), ('1', '1'), ('0', '0'), ('5', '5'), ('2', '2')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(choices=[('0', 'INFT'), ('1', 'CMPN'), ('2', 'EXTC'), ('3', 'ETRX'), ('4', 'BIOM')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='div',
            field=models.CharField(choices=[('0', 'A'), ('1', 'B'), ('2', 'C')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('0', 'Male'), ('1', 'Female'), ('2', 'Other')], max_length=15, null=True),
        ),
    ]
