# Generated by Django 3.2.4 on 2021-06-30 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMS_Student', '0019_alter_student_roll_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.CharField(default='', max_length=123, null=True),
        ),
    ]
