# Generated by Django 3.2.4 on 2021-06-30 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMS_Student', '0017_auto_20210701_0020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('roll_no', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
