from django.db import models
from django.core.validators import MaxValueValidator
# from django.contrib.auth.models import User

class Student(models.Model):
    roll_no = models.CharField(primary_key=True ,max_length=20, null=False)
    phone = models.CharField(max_length=10, null=True)
    father_name = models.CharField(max_length=50, null=True)
    skills = models.TextField(max_length=500, null=False)

    def __str__(self):
        return self.roll_no

class Add_edu(models.Model):
    degree_choice = {
        ('10', '10th'),
        ('12', '12th'),
        ('diploma', 'Diploma')
    }
    clg_name = models.CharField(max_length=50,null=False)
    degree = models.CharField(max_length=50, choices=degree_choice, null=True)
    board = models.CharField(max_length=50)
    percentage = models.FloatField(null=False)
    start_year= models.DateField(null=False)
    end_year = models.DateField(null=False)
    roll_no = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.clg_name


class Add_exp(models.Model):
    comp_name = models.CharField(max_length=50, null=False)
    role = models.CharField(max_length=50, null=False)
    duration = models.CharField(max_length=50, null=False)
    rollNo = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    start_date = models.DateField(null=False)

    def __str__(self):
        return self.comp_name

class FE(models.Model):
    roll_no_1 = models.ForeignKey(Student ,on_delete=models.CASCADE)
    fe_sem1_sgpa = models.FloatField(validators=[MaxValueValidator(10)])
    fe_sem2_sgpa = models.FloatField(validators=[MaxValueValidator(10)])
    fe_cgpa = models.FloatField(validators=[MaxValueValidator(10)])

    def __str__(self):
        return self.roll_no_1

class SE(models.Model):
    roll_no_2 = models.ForeignKey(Student ,on_delete=models.CASCADE)
    se_sem3_sgpa = models.FloatField(validators=[MaxValueValidator(10)])
    se_sem4_sgpa = models.FloatField(validators=[MaxValueValidator(10)])
    se_cgpa = models.FloatField()

    def __str__(self):
        return self.roll_no_2


class TE(models.Model):
    roll_no_3 = models.ForeignKey(Student ,on_delete=models.CASCADE)
    te_sem5_sgpa = models.FloatField(validators=[MaxValueValidator(10)])
    te_sem6_sgpa = models.FloatField(validators=[MaxValueValidator(10)])
    te_cgpa = models.FloatField(validators=[MaxValueValidator(10)])

    def __str__(self):
        return self.roll_no_3

class BE(models.Model):
    roll_no_4 = models.ForeignKey(Student ,on_delete=models.CASCADE)
    be_sem7_sgpa = models.FloatField(validators=[MaxValueValidator(10)])
    be_sem8_sgpa = models.FloatField(validators=[MaxValueValidator(10)])
    be_cgpa = models.FloatField(validators=[MaxValueValidator(10)])

    def __str__(self):
        return self.roll_no_4


class AdminDma(models.Model):
    name = models.CharField(max_length=30, null=False)
    department = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name


class Intership(models.Model):
    comp_name = models.CharField(max_length=40,null=False)
    link =models.CharField(max_length=150,null=False)
    start_date = models.DateField(null=False)
    apply_by =models.DateField(null=False)
    sal =models.IntegerField(null=False)
    skills=models.TextField(max_length=500, null=False)
    duration =models.CharField(max_length=20, null=False)
    adm_id = models.ForeignKey(AdminDma, on_delete=models.CASCADE, null=False)
    domain=models.CharField(max_length=100,null=False)
    about_comp=models.TextField(max_length=500, null=False)
    about_work =models.TextField(max_length=500, null=False)
    who_can_apply=models.TextField(max_length=500, null=False)
    perks=models.TextField(max_length=500, null=False)
    additional=models.TextField(max_length=500, null=False)
    work_from_home = models.BooleanField(default=False)

    def __str__(self):
        return self.comp_name

class Int_user(models.Model):
    status = models.CharField(max_length=10, null=False)
    roll_no = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    int_id = models.ForeignKey(Intership, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return str(self.roll_no)

class Job(models.Model):
    comp_name = models.CharField(max_length=40, null=False)
    location = models.CharField(max_length=100)
    link = models.CharField(max_length=150, null=False)
    start_date = models.DateField(null=False)
    apply_by = models.DateField(null=True)
    sal = models.IntegerField(null=False)
    skills = models.TextField(max_length=500, null=False)
    domain = models.CharField(max_length=100)
    adm_id = models.ForeignKey(AdminDma, on_delete=models.CASCADE, null=False)
    about_comp = models.TextField(max_length=500, null=False)
    about_work = models.TextField(max_length=500, null=False)
    who_can_apply = models.TextField(max_length=500, null=False)
    perks = models.TextField(max_length=500, null=False)
    additional = models.TextField(max_length=500, null=False)
    status=models.CharField(max_length=10, null=True,default=0)
    work_from_home = models.BooleanField(default=False)

    def __str__(self):
        return self.comp_name

class Job_user(models.Model):
    status = models.CharField(max_length=10, null=False)
    roll_no = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.roll_no)


class Mock_test(models.Model):
    name = models.CharField(max_length=30, null=True)
    date = models.DateField(null=False)
    adm_id = models.ForeignKey(AdminDma, on_delete=models.CASCADE, null=False)
    from_time = models.TimeField()
    to_time = models.TimeField()
    details = models.TextField(max_length=500, null=False)
    link = models.CharField(max_length=50, null=False, default="https")


    def __str__(self):
        return self.name