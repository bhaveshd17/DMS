# Generated by Django 3.2.4 on 2021-07-07 14:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMS_Student', '0006_auto_20210707_1937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curredu',
            old_name='be_sgpa7',
            new_name='be_sgpi7',
        ),
        migrations.RenameField(
            model_name='curredu',
            old_name='be_sgpa8',
            new_name='be_sgpi8',
        ),
        migrations.RenameField(
            model_name='curredu',
            old_name='fe_sgpa1',
            new_name='fe_sgpi1',
        ),
        migrations.RenameField(
            model_name='curredu',
            old_name='fe_sgpa2',
            new_name='fe_sgpi2',
        ),
        migrations.RenameField(
            model_name='curredu',
            old_name='se_sgpa3',
            new_name='se_sgpi3',
        ),
        migrations.RenameField(
            model_name='curredu',
            old_name='se_sgpa4',
            new_name='se_sgpi4',
        ),
        migrations.RenameField(
            model_name='curredu',
            old_name='te_sgpa5',
            new_name='te_sgpi5',
        ),
        migrations.RenameField(
            model_name='curredu',
            old_name='te_sgpa6',
            new_name='te_sgpi6',
        ),
        migrations.AddField(
            model_name='curredu',
            name='average_sgpi',
            field=models.FloatField(null=True, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='curredu',
            name='total_grade',
            field=models.FloatField(null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='add_edu',
            name='degree',
            field=models.CharField(choices=[('diploma', 'Diploma'), ('10', '10th'), ('12', '12th')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='add_edu',
            name='diploma_pattern',
            field=models.CharField(choices=[('semester pattern', 'semester pattern'), ('NA', 'NA'), ('yearly pattern', 'yearly pattern')], default='NA', max_length=20),
        ),
        migrations.AlterField(
            model_name='add_edu',
            name='gap',
            field=models.CharField(choices=[('4', '4'), ('1', '1'), ('5', '5'), ('2', '2'), ('0', '0'), ('3', '3')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='curredu',
            name='dead_kt',
            field=models.CharField(choices=[('1', '1'), ('7', 'Greater than 6'), ('6', '6'), ('4', '4'), ('5', '5'), ('2', '2'), ('0', '0'), ('3', '3')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='curredu',
            name='drop',
            field=models.CharField(choices=[('1', '1'), ('3', 'Greater than 2'), ('0', '0'), ('2', '2')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='curredu',
            name='live_kt',
            field=models.CharField(choices=[('1', '1'), ('7', 'Greater than 6'), ('6', '6'), ('4', '4'), ('5', '5'), ('2', '2'), ('0', '0'), ('3', '3')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='drop',
            field=models.CharField(choices=[('1', '1'), ('3', 'Greater than 2'), ('0', '0'), ('2', '2')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='live_kt',
            field=models.CharField(choices=[('1', '1'), ('7', 'Greater than 6'), ('6', '6'), ('4', '4'), ('5', '5'), ('2', '2'), ('0', '0'), ('3', '3')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(choices=[('0', 'CMPN'), ('3', 'ETRX'), ('2', 'EXTC'), ('1', 'INFT'), ('4', 'BIOM')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('1', 'Female'), ('2', 'Other'), ('0', 'Male')], max_length=15, null=True),
        ),
    ]
