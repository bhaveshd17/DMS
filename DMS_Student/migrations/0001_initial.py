# Generated by Django 3.2.5 on 2021-09-06 15:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
                ('work_from_home', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField(max_length=40)),
                ('location', models.CharField(max_length=100)),
                ('recruiting_from', models.CharField(default='NA', max_length=500, null=True)),
                ('link', models.CharField(max_length=150)),
                ('start_date', models.DateField()),
                ('apply_by', models.DateField(null=True)),
                ('sal', models.FloatField(validators=[django.core.validators.MaxValueValidator(99)])),
                ('skills', models.TextField(max_length=500)),
                ('domain', models.CharField(max_length=100)),
                ('about_comp', models.TextField(max_length=500)),
                ('about_work', models.TextField(max_length=500)),
                ('aggregate_sgpi', models.CharField(max_length=15, null=True)),
                ('ssc_percentage', models.CharField(max_length=15, null=True)),
                ('hsc_d_percentage', models.CharField(max_length=15, null=True)),
                ('live_kt', models.CharField(max_length=15, null=True)),
                ('dead_kt', models.CharField(max_length=15, null=True)),
                ('drop', models.CharField(choices=[('0', '0 year'), ('1', '1 year'), ('2', '2 years'), ('3', '3 years'), ('4', '4 years'), ('5', '5 years')], max_length=15, null=True)),
                ('who_can_apply', models.TextField(max_length=500)),
                ('perks', models.TextField(max_length=500)),
                ('additional', models.TextField(max_length=500)),
                ('status', models.CharField(default=0, max_length=10, null=True)),
                ('work_from_home', models.BooleanField(default=False)),
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
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('skills', models.TextField(max_length=500)),
                ('age', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99)])),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=15, null=True)),
                ('branch', models.CharField(choices=[('BIOM', 'BIOM'), ('CMPN', 'CMPN'), ('ETRX', 'ETRX'), ('EXTC', 'EXTC'), ('INFT', 'INFT')], max_length=12, null=True)),
                ('div', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=12, null=True)),
                ('corresponding_address', models.TextField(max_length=500, null=True)),
                ('permanent_address', models.TextField(max_length=500, null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('gmail', models.EmailField(max_length=254, null=True)),
                ('residence_phone', models.CharField(max_length=10, null=True)),
                ('pan_card_no', models.CharField(max_length=10, null=True)),
                ('aadhar_no', models.CharField(max_length=12, null=True)),
                ('passport_no', models.CharField(max_length=9, null=True)),
                ('year_of_graduation', models.CharField(max_length=4, null=True)),
                ('disability', models.BooleanField(null=True)),
                ('type_of_disability', models.CharField(max_length=100, null=True)),
                ('father_name', models.CharField(max_length=50, null=True)),
                ('mother_name', models.CharField(max_length=50, null=True)),
                ('father_occupation', models.CharField(max_length=50, null=True)),
                ('mother_occupation', models.CharField(max_length=50, null=True)),
                ('co_curriculum_activities', models.CharField(max_length=100, null=True)),
                ('extra_curriculum_activities', models.CharField(max_length=100, null=True)),
                ('hobbies', models.CharField(max_length=150, null=True)),
                ('profile_photo', models.ImageField(null=True, upload_to='profile/')),
                ('resume', models.FileField(null=True, upload_to='Resume/')),
                ('facebook', models.URLField(null=True)),
                ('linkdin', models.URLField(null=True)),
                ('github', models.URLField(null=True)),
                ('other', models.CharField(max_length=150, null=True)),
                ('is_email_verified', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_mail_send', models.BooleanField(default=False, null=True)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DMS_Student.job')),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DMS_Student.student')),
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
            name='CurrEdu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sgpi1', models.CharField(default='NA', max_length=4)),
                ('sgpi2', models.CharField(default='NA', max_length=4)),
                ('cgpa1', models.CharField(default='NA', max_length=4)),
                ('sgpi3', models.CharField(default='NA', max_length=4)),
                ('sgpi4', models.CharField(default='NA', max_length=4)),
                ('cgpa2', models.CharField(default='NA', max_length=4)),
                ('sgpi5', models.CharField(default='NA', max_length=4)),
                ('sgpi6', models.CharField(default='NA', max_length=4)),
                ('cgpa3', models.CharField(default='NA', max_length=4)),
                ('sgpi7', models.CharField(default='NA', max_length=4)),
                ('sgpi8', models.CharField(default='NA', max_length=4)),
                ('cgpa4', models.CharField(default='NA', max_length=4)),
                ('live_kt', models.CharField(max_length=15, null=True)),
                ('dead_kt', models.CharField(max_length=15, null=True)),
                ('drop', models.CharField(choices=[('0', '0 year'), ('1', '1 year'), ('2', '2 years'), ('3', '3 years'), ('4', '4 years'), ('5', '5 years')], max_length=15, null=True)),
                ('total_grade', models.FloatField(default=0, null=True, validators=[django.core.validators.MaxValueValidator(100)])),
                ('average_sgpi', models.FloatField(default=0, null=True, validators=[django.core.validators.MaxValueValidator(10)])),
                ('roll_no_curr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DMS_Student.student')),
            ],
        ),
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_name', models.CharField(max_length=500)),
                ('domain', models.CharField(max_length=500)),
                ('file', models.FileField(upload_to='documents/%Y-%m-%d')),
                ('certificate_issued_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DMS_Student.student')),
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
                ('rollNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DMS_Student.student')),
            ],
        ),
        migrations.CreateModel(
            name='Add_edu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clg_name', models.CharField(max_length=50)),
                ('degree', models.CharField(choices=[('10', '10th'), ('12', '12th'), ('diploma', 'Diploma')], max_length=50, null=True)),
                ('no_of_subject', models.CharField(max_length=20, null=True)),
                ('board', models.CharField(max_length=50)),
                ('percentage', models.FloatField()),
                ('start_year', models.DateField()),
                ('end_year', models.DateField()),
                ('marks', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('gap', models.CharField(choices=[('0', '0 year'), ('1', '1 year'), ('2', '2 years'), ('3', '3 years'), ('4', '4 years'), ('5', '5 years')], max_length=15, null=True)),
                ('diploma_pattern', models.CharField(choices=[('semester pattern', 'semester pattern'), ('NA', 'NA'), ('yearly pattern', 'yearly pattern')], default='NA', max_length=20)),
                ('diploma_aggregate_mw', models.CharField(default='NA', max_length=100)),
                ('diploma_aggregate_pw', models.CharField(default='NA', max_length=100)),
                ('no_of_dead_kt', models.CharField(default='NA', max_length=10)),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DMS_Student.student')),
            ],
        ),
    ]
