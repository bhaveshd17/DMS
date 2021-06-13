from django.db import models

class add_edu(models.Model):
    clg_name = models.CharField(max_length=50,null=False)
    degree = models.CharField(max_length=50,null=False)
    marks =model.IntegerField(max_length=11,null=False)
    start_year= model.DateField(null=False)
    end_year =models.DateField(null=False)
    roll_no =models.IntegerField(null=False)

def __str__(self):
    return self.roll_no

class add_exp(models.Model):
    comp_name = models.CharField(max_length=50, null=False)
    role = models.CharField(max_length=50, null=False)
    duration = models.CharField(max_length=50, null=False)
    roll_no = models.CharField(max_length=20, null=False)
    start_date = models.DateField(null=False)

def _str_(self):
    return self.id

class admin(models.Model):
    name = models.CharField(max_length=30, null=False)
    department = models.CharField(max_length=30, null=False)

def _str_(self):
    return self.name

class intership(models.Model):
    comp_name = models.CharField(max_length=40,null=False)
    link =models.CharField(max_length=150,null=False)
    start_date = models.DateField(null=False)
    apply_by =models.DateField(null=False)
    sal =models.IntegerField(max_length=11,null=False)
    skills=models.IntegerField(null=False)
    duration =models.IntegerField(max_length=20,null=False)
    adm_id =models.IntegerField(max_length=11,null=False)
    domain=models.CharField(max_length=100,null=False)
    about_comp=models.CharField(null=False)
    about_work =models.CharField(null=False)
    who_can_apply=models.CharField(null=False)
    perks=models.CharField(null=False)
    additional=models.CharField(null=False)

def __str__(self):
    return self.comp_name

class int_user(models.Model):
    status = models.CharField(max_length=10, null=False)
    roll_no = models.CharField(max_length=10, null=False)
    int_id = models.IntegerField()

def _str_(self):
     return self.roll_no

class job(models.Model):
    comp_name = models.CharField(max_length=40, null=False)
    link = models.CharField(max_length=150, null=False)
    start_date = models.DateField(null=False)
    apply_by = models.DateField(null=True)
    sal = models.IntegerField(null=False)
    skill = models.TextField(max_length=500, null=False)
    domain = models.CharField(max_length=100)
    adm_id = models.IntegerField()
    about_comp = models.TextField(max_length=500, null=False)
    about_work = models.TextField(max_length=500, null=False)
    who_can_apply = models.TextField(max_length=500, null=False)
    perk = models.TextField(max_length=500, null=False)
    additional = models.TextField(max_length=500, null=False)
    
def _str_(self):
    return self.comp_name