# Generated by Django 3.2.5 on 2021-08-15 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMS_Student', '0005_auto_20210805_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='intership',
            name='adm_id',
        ),
        migrations.RemoveField(
            model_name='job',
            name='adm_id',
        ),
        migrations.RemoveField(
            model_name='mock_test',
            name='adm_id',
        ),
        migrations.AlterField(
            model_name='add_edu',
            name='diploma_pattern',
            field=models.CharField(choices=[('semester pattern', 'semester pattern'), ('yearly pattern', 'yearly pattern'), ('NA', 'NA')], default='NA', max_length=20),
        ),
        migrations.DeleteModel(
            name='AdminDma',
        ),
    ]
