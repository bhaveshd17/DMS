# Generated by Django 3.2.4 on 2021-06-30 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMS_Student', '0031_auto_20210701_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.CharField(default=1, max_length=100, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
