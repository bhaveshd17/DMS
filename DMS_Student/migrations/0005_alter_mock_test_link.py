# Generated by Django 3.2.4 on 2021-06-14 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMS_Student', '0004_mock_test_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mock_test',
            name='link',
            field=models.CharField(default='https', max_length=50),
        ),
    ]
