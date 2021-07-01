# Generated by Django 3.2.4 on 2021-06-30 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminDma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField(max_length=40)),
                ('location', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=150)),
                ('start_date', models.DateField()),
                ('apply_by', models.DateField(null=True)),
                ('sal', models.IntegerField()),
                ('skills', models.TextField(max_length=500)),
                ('domain', models.CharField(max_length=100)),
                ('about_comp', models.TextField(max_length=500)),
                ('about_work', models.TextField(max_length=500)),
                ('who_can_apply', models.TextField(max_length=500)),
                ('perks', models.TextField(max_length=500)),
                ('additional', models.TextField(max_length=500)),
                ('adm_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DMS_Student.admindma')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('skills', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Mock_test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('date', models.DateField()),
                ('from_time', models.TimeField()),
                ('to_time', models.TimeField()),
                ('details', models.TextField(max_length=500)),
                ('link', models.CharField(default='https', max_length=50)),
                ('adm_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DMS_Student.admindma')),
            ],
        ),
        migrations.CreateModel(
            name='Job_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DMS_Student.job')),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DMS_Student.student')),
            ],
        ),
        migrations.CreateModel(
            name='Intership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField(max_length=40)),
                ('link', models.CharField(max_length=150)),
                ('start_date', models.DateField()),
                ('apply_by', models.DateField()),
                ('sal', models.IntegerField()),
                ('skills', models.TextField(max_length=500)),
                ('duration', models.CharField(max_length=20)),
                ('domain', models.CharField(max_length=100)),
                ('about_comp', models.TextField(max_length=500)),
                ('about_work', models.TextField(max_length=500)),
                ('who_can_apply', models.TextField(max_length=500)),
                ('perks', models.TextField(max_length=500)),
                ('additional', models.TextField(max_length=500)),
                ('adm_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DMS_Student.admindma')),
            ],
        ),
        migrations.CreateModel(
            name='Int_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('int_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DMS_Student.intership')),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DMS_Student.student')),
            ],
        ),
        migrations.CreateModel(
            name='Add_exp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DMS_Student.student')),
            ],
        ),
        migrations.CreateModel(
            name='Add_edu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clg_name', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=50)),
                ('marks', models.IntegerField()),
                ('start_year', models.DateField()),
                ('end_year', models.DateField()),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DMS_Student.student')),
            ],
        ),
    ]
