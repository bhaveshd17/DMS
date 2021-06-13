from django.db import models
# from django.contrib.auth.models import User

class Student(models.Model):
    roll_no = models.CharField(primary_key=True ,max_length=20, null=False)
    name = models.CharField(max_length=50, null=False)
    skills = models.TextField(max_length=500, null=False)

    def __str__(self):
        return self.roll_no

class Add_edu(models.Model):
    clg_name = models.CharField(max_length=50,null=False)
    degree = models.CharField(max_length=50,null=False)
    marks = models.IntegerField(null=False)
    start_year= models.DateField(null=False)
    end_year = models.DateField(null=False)
    roll_no = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.clg_name

class Add_exp(models.Model):
    comp_name = models.CharField(max_length=50, null=False)
    role = models.CharField(max_length=50, null=False)
    duration = models.CharField(max_length=50, null=False)
    roll_no = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    start_date = models.DateField(null=False)

    def __str__(self):
        return str(self.id)

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

    def __str__(self):
        return self.comp_name

class Int_user(models.Model):
    status = models.CharField(max_length=10, null=False)
    roll_no = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    int_id = models.ForeignKey(Intership, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.roll_no

class Job(models.Model):
    comp_name = models.CharField(max_length=40, null=False)
    link = models.CharField(max_length=150, null=False)
    start_date = models.DateField(null=False)
    apply_by = models.DateField(null=True)
    sal = models.IntegerField(null=False)
    skill = models.TextField(max_length=500, null=False)
    domain = models.CharField(max_length=100)
    adm_id = models.ForeignKey(AdminDma, on_delete=models.CASCADE, null=False)
    about_comp = models.TextField(max_length=500, null=False)
    about_work = models.TextField(max_length=500, null=False)
    who_can_apply = models.TextField(max_length=500, null=False)
    perk = models.TextField(max_length=500, null=False)
    additional = models.TextField(max_length=500, null=False)

    def __str__(self):
        return self.comp_name

class Job_user(models.Model):
    status = models.CharField(max_length=10, null=False)
    roll_no = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.roll_no

class Login(models.Model):
    roll_no = models.CharField(primary_key=True, max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.roll_no

class Mock_test(models.Model):
    name = models.CharField(max_length=30, null=False)
    date = models.DateField(null=False)
    adm_id = models.ForeignKey(AdminDma, on_delete=models.CASCADE, null=False)
    from_time = models.TimeField()
    to_time = models.TimeField()
    details = models.TextField(max_length=500, null=False)

    def __str__(self):
        return self.name

