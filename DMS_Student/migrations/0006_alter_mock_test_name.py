# Generated by Django 3.2.4 on 2021-06-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMS_Student', '0005_alter_mock_test_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mock_test',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]