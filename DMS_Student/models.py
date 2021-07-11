from re import T
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator


class Student(models.Model):
    roll_no = models.CharField(primary_key=True ,max_length=20, null=False)
    phone = models.CharField(max_length=10, null=True)
    skills = models.TextField(max_length=500, null=False)
    age=models.IntegerField(validators=[MaxValueValidator(99)],null=True)
    gender=models.CharField(max_length=15,choices={
        ("0","Male"),("1","Female"),("2","Other")
    },null=True)
    branch=models.CharField(max_length=12,choices={
        ("0","CMPN"),("1","INFT"),("2","EXTC"),("3","ETRX"),("4","BIOM")
    },null=True)
    div=models.CharField(max_length=12,choices={
        ("0","A"),("1","B"),("2","C")
    },null=True)
    corresponding_address=models.TextField(max_length=500,null=True)
    permanent_address=models.TextField(max_length=500,null=True)
    date_of_birth=models.DateField(null=True)
    gmail=models.EmailField(null=True)
    residence_phone= models.CharField(max_length=10, null=True)
    pan_card_no=models.CharField(max_length=20,null=True)
    aadhar_no=models.CharField(max_length=20,null=True)
    passport_no=models.CharField(max_length=20,null=True)
    year_of_graduation=models.CharField(max_length=4,null=True)
    disability=models.BooleanField(null=True)
    type_of_disability=models.CharField(max_length=100,null=True)
    father_name = models.CharField(max_length=50, null=True)
    mother_name=models.CharField(max_length=50,null=True)
    father_occupation=models.CharField(max_length=50,null=True)
    mother_occupation=models.CharField(max_length=50,null=True)
    co_curriculum_activities=models.CharField(max_length=100,null=True)
    extra_curriculum_activities=models.CharField(max_length=100,null=True)
    hobbies=models.CharField(max_length=150,null=True)
    profile_photo=models.ImageField(upload_to="profile/",null=True)
    resume=models.FileField(null=True)
    facebook=models.URLField(null=True)
    linkdin=models.URLField(null=True)
    github=models.URLField(null=True)
    other=models.CharField(max_length=150,null=True)
    is_email_verified=models.BooleanField(default=False,null=True)

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
    marks = models.IntegerField(validators=[MaxValueValidator(999)])
    roll_no = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    gap=models.CharField(max_length=15,choices={
        ("0","0"),("1","1"),("2","2"),("3","3"),("4","4"),("5","5")
    },null=True)

    diploma_pattern = models.CharField(max_length=20, choices={
        ("semester pattern","semester pattern"), ("yearly pattern","yearly pattern"), ("NA", "NA")
    }, default="NA")
    diploma_aggregate_mw = models.CharField(max_length=100, default="NA")
    diploma_aggregate_pw = models.CharField(max_length=100, default="NA")
    no_of_dead_kt = models.CharField(max_length=10, default="NA")

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
        return str(self.roll_no_1)

class SE(models.Model):
    roll_no_2 = models.ForeignKey(Student ,on_delete=models.CASCADE)
    se_sem3_sgpa = models.FloatField(validators=[MaxValueValidator(10)])
    se_sem4_sgpa = models.FloatField(validators=[MaxValueValidator(10)])
    se_cgpa = models.FloatField()

    def __str__(self):
        return str(self.roll_no_2)


class TE(models.Model):
    roll_no_3 = models.ForeignKey(Student ,on_delete=models.CASCADE)
    te_sem5_sgpa = models.FloatField(validators=[MaxValueValidator(10)])
    te_sem6_sgpa = models.FloatField(validators=[MaxValueValidator(10)])
    te_cgpa = models.FloatField(validators=[MaxValueValidator(10)])
    live_kt=models.CharField(max_length=15,null=True)
    drop=models.CharField(max_length=15,choices={
        ("0","0"),("1","1"),("2","2"),("3","3"),("4","4"),("5","5")
    },null=True)
    dead_kt=models.CharField(max_length=15,null=True)
    def __str__(self):
        return str(self.roll_no_3)

class BE(models.Model):
    roll_no_4 = models.ForeignKey(Student ,on_delete=models.CASCADE)
    be_sem7_sgpa = models.FloatField(validators=[MaxValueValidator(10)])
    be_sem8_sgpa = models.FloatField(validators=[MaxValueValidator(10)])
    be_cgpa = models.FloatField(validators=[MaxValueValidator(10)])
    kt_BE=models.CharField(max_length=15,choices={
        ("0","0"),("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","Greater than 6")

    },null=True)
    drop_BE=models.CharField(max_length=15,choices={
        ("0","0"),("1","1"),("2","2"),("3","Greater than 2")
    },null=True)
    def __str__(self):
        return str(self.roll_no_4)


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
    sal = models.FloatField(null=False,validators=[MaxValueValidator(99)])
    skills = models.TextField(max_length=500, null=False)
    domain = models.CharField(max_length=100)
    adm_id = models.ForeignKey(AdminDma, on_delete=models.CASCADE, null=False)
    about_comp = models.TextField(max_length=500, null=False)
    about_work = models.TextField(max_length=500, null=False)
    cgpa=models.FloatField(validators=[MaxValueValidator(10)])
    live_kt=models.CharField(max_length=15,choices={
        ("0", "0"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"), ("6", "6"), ("7", "Greater than 6")

    },null=True)
    drop=models.CharField(max_length=15,choices={
        ("0", "0"), ("1", "1"), ("2", "2"), ("3", "Greater than 2")
    },null=True)
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

class Certificates(models.Model):
    certificate_name = models.CharField(max_length=500)
    domain = models.CharField(max_length=500)
    file = models.FileField(upload_to='documents/%Y-%m-%d')
    certificate_issued_to = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.certificate_name
