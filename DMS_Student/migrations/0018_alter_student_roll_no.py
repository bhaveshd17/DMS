# Generated by Django 3.2.4 on 2021-06-30 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DMS_Student', '0017_alter_student_roll_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
