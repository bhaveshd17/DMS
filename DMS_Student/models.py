from django.db import models
from django.core.validators import MaxValueValidator
from typing import LiteralString


class Student(models.Model):
    roll_no: LiteralString = models.CharField(primary_key=True, max_length=20, null=False)
    phone: LiteralString = models.CharField(max_length=10, null=True)
    skills: LiteralString = models.TextField(max_length=500, null=False)
    age = models.IntegerField(validators=[MaxValueValidator(99)], null=True)
    gender: LiteralString = models.CharField(max_length=15, choices=sorted({
        ("Male", "Male"), ("Female", "Female"), ("Other", "Other")
    }), null=True)
    branch: LiteralString = models.CharField(max_length=12, choices=sorted({
        ("INFT", "INFT"), ("CMPN", "CMPN"), ("EXTC", "EXTC"), ("ETRX", "ETRX"), ("BIOM", "BIOM")
    }), null=True)
    div: LiteralString = models.CharField(max_length=12, choices=sorted({
        ("A", "A"), ("B", "B"), ("C", "C")
    }), null=True)
    corresponding_address: LiteralString = models.TextField(max_length=500, null=True)
    permanent_address: LiteralString = models.TextField(max_length=500, null=True)
    date_of_birth = models.DateField(null=True)
    gmail = models.EmailField(null=True)
    residence_phone: LiteralString = models.CharField(max_length=10, null=True)
    pan_card_no: LiteralString = models.CharField(max_length=10, null=True)
    aadhar_no: LiteralString = models.CharField(max_length=12, null=True)
    passport_no: LiteralString = models.CharField(max_length=9, null=True)
    year_of_graduation = models.IntegerField(null=True, db_index=True)
    disability = models.BooleanField(null=True)
    type_of_disability: LiteralString = models.CharField(max_length=100, null=True)
    father_name: LiteralString = models.CharField(max_length=50, null=True)
    mother_name: LiteralString = models.CharField(max_length=50, null=True)
    father_occupation: LiteralString = models.CharField(max_length=50, null=True)
    mother_occupation: LiteralString = models.CharField(max_length=50, null=True)
    co_curriculum_activities: LiteralString = models.CharField(max_length=100, null=True)
    extra_curriculum_activities: LiteralString = models.CharField(max_length=100, null=True)
    hobbies: LiteralString = models.CharField(max_length=150, null=True)
    profile_photo = models.ImageField(upload_to="profile/", null=True)
    resume = models.FileField(upload_to="Resume/", null=True)
    facebook = models.URLField(null=True)
    linkdin = models.URLField(null=True)
    github = models.URLField(null=True)
    other: LiteralString = models.CharField(max_length=150, null=True)
    placed = models.BooleanField(default=False, null=True)
    is_email_verified = models.BooleanField(default=False, null=True)

    def __str__(self) -> str:
        return self.roll_no


class Add_edu(models.Model):
    degree_choice = sorted({
        ('10', '10th'),
        ('12', '12th'),
        ('diploma', 'Diploma')
    })
    clg_name: LiteralString = models.CharField(max_length=50, null=False)
    degree: LiteralString = models.CharField(max_length=50, choices=degree_choice, null=True)
    no_of_subject: LiteralString = models.CharField(max_length=20, null=True)
    board: LiteralString = models.CharField(max_length=50, null=True)
    percentage = models.FloatField(null=False)
    start_year = models.DateField(null=False)
    end_year = models.DateField(null=False)
    marks = models.IntegerField(validators=[MaxValueValidator(999)])
    roll_no = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    gap: LiteralString = models.CharField(max_length=15, choices=sorted({
        ("0", "0 year"), ("1", "1 year"), ("2", "2 years"), ("3", "3 years"), ("4", "4 years"), ("5", "5 years")
    }), null=True)

    diploma_pattern: LiteralString = models.CharField(max_length=20, choices={
        ("semester pattern", "semester pattern"), ("yearly pattern", "yearly pattern"), ("NA", "NA")
    }, default="NA")
    diploma_aggregate_mw: LiteralString = models.CharField(max_length=100, default="NA")
    diploma_aggregate_pw: LiteralString = models.CharField(max_length=100, default="NA")
    no_of_dead_kt: LiteralString = models.CharField(max_length=10, default="NA")

    def __str__(self) -> str:
        return self.clg_name


class Add_exp(models.Model):
    comp_name: LiteralString = models.CharField(max_length=50, null=False)
    role: LiteralString = models.CharField(max_length=50, null=False)
    duration: LiteralString = models.CharField(max_length=50, null=False)
    rollNo = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    start_date = models.DateField(null=False)

    def __str__(self) -> str:
        return self.comp_name


class CurrEdu(models.Model):
    roll_no_curr = models.ForeignKey(Student, on_delete=models.CASCADE)
    sgpi1: LiteralString = models.CharField(max_length=4, default="NA")
    sgpi2: LiteralString = models.CharField(max_length=4, default="NA")
    cgpa1: LiteralString = models.CharField(max_length=4, default="NA")
    sgpi3: LiteralString = models.CharField(max_length=4, default="NA")
    sgpi4: LiteralString = models.CharField(max_length=4, default="NA")
    cgpa2: LiteralString = models.CharField(max_length=4, default="NA")
    sgpi5: LiteralString = models.CharField(max_length=4, default="NA")
    sgpi6: LiteralString = models.CharField(max_length=4, default="NA")
    cgpa3: LiteralString = models.CharField(max_length=4, default="NA")
    sgpi7: LiteralString = models.CharField(max_length=4, default="NA")
    sgpi8: LiteralString = models.CharField(max_length=4, default="NA")
    cgpa4: LiteralString = models.CharField(max_length=4, default="NA")
    live_kt: LiteralString = models.CharField(max_length=15, null=True)
    dead_kt: LiteralString = models.CharField(max_length=15, null=True)
    drop: LiteralString = models.CharField(max_length=15, choices=sorted({
        ("0", "0 year"), ("1", "1 year"), ("2", "2 years"), ("3", "3 years"), ("4", "4 years"), ("5", "5 years")
    }), null=True)
    total_grade = models.FloatField(validators=[MaxValueValidator(100)], null=True, default=0)
    average_sgpi = models.FloatField(validators=[MaxValueValidator(10)], null=True, default=0)

    def __str__(self) -> str:
        return str(self.roll_no_curr)


class Intership(models.Model):
    comp_name: LiteralString = models.CharField(max_length=40, null=False)
    link: LiteralString = models.CharField(max_length=150, null=False)
    start_date = models.DateField(null=False)
    apply_by = models.DateField(null=False)
    sal = models.IntegerField(null=False)
    skills: LiteralString = models.TextField(max_length=500, null=False)
    duration: LiteralString = models.CharField(max_length=20, null=False)
    domain: LiteralString = models.CharField(max_length=100, null=False)
    about_comp: LiteralString = models.TextField(max_length=500, null=False)
    about_work: LiteralString = models.TextField(max_length=500, null=False)
    who_can_apply: LiteralString = models.TextField(max_length=500, null=False)
    perks: LiteralString = models.TextField(max_length=500, null=False)
    additional: LiteralString = models.TextField(max_length=500, null=False)
    work_from_home = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.comp_name


class Int_user(models.Model):
    status: LiteralString = models.CharField(max_length=10, null=False)
    roll_no = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    int_id = models.ForeignKey(Intership, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return str(self.roll_no)


class Job(models.Model):
    comp_name: LiteralString = models.CharField(max_length=40, null=False)
    location: LiteralString = models.CharField(max_length=100)
    recruiting_from: LiteralString = models.CharField(max_length=500, null=True, default="NA")
    link: LiteralString = models.CharField(max_length=150, null=False)
    year: LiteralString = models.CharField(max_length=25, null=True, blank=True)
    apply_by = models.DateField(null=True)
    sal: LiteralString = models.CharField(null=False, max_length=150)
    skills: LiteralString = models.TextField(max_length=500, null=False)
    domain: LiteralString = models.CharField(max_length=100, choices=sorted({
        ("Automotive", "Automotive"), ("Banking", "Banking"), ("EduTech", "EduTech"), ("Financial Services", "Financial Services"),
        ("Information Technology", "Information Technology"), ("Logistics & Supply Chain", "Logistics & Supply Chain"),
        ("Retail", "Retail"), ("Telecommunications", "Telecommunications"), ("Electrical Manufacturing", "Electrical Manufacturing"),
        ("Marketing & Advertising", "Marketing & Advertising"), ("Media Production", "Media Production"),
        ("Management Consulting", "Management Consulting"), ("Manufacturing", "Manufacturing"), ("Health Care", "Health Care"),
        ("Design", "Design"), ("Professional Services", "Professional Services")
    }))
    about_comp: LiteralString = models.TextField(max_length=500, null=False)
    about_work: LiteralString = models.TextField(max_length=500, null=False)
    aggregate_sgpi: LiteralString = models.CharField(max_length=15, null=True)
    ssc_percentage: LiteralString = models.CharField(max_length=15, null=True)
    hsc_d_percentage: LiteralString = models.CharField(max_length=15, null=True)
    live_kt: LiteralString = models.CharField(max_length=15, null=True)
    dead_kt: LiteralString = models.CharField(max_length=15, null=True)
    drop: LiteralString = models.CharField(max_length=15, choices=sorted({
        ("0", "0 year"), ("1", "1 year"), ("2", "2 years"), ("3", "3 years"), ("4", "4 years"), ("5", "5 years")
    }), null=True)
    who_can_apply: LiteralString = models.TextField(max_length=500, null=True, blank=True)
    perks: LiteralString = models.TextField(max_length=500, null=False)
    additional: LiteralString = models.TextField(max_length=500, null=False)
    status: LiteralString = models.CharField(max_length=10, null=True, default=0)
    work_from_home = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.comp_name


class Job_user(models.Model):
    status: LiteralString = models.CharField(max_length=10, null=False)
    roll_no = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now_add=True, null=True)
    salary: LiteralString = models.CharField(max_length=50, null=True)
    is_mail_send = models.BooleanField(default=False, null=True)

    def __str__(self) -> str:
        return str(self.roll_no) + "," + str(self.job_id)


class Mock_test(models.Model):
    name: LiteralString = models.CharField(max_length=30, null=True)
    date = models.DateField(null=False)
    from_time = models.TimeField()
    to_time = models.TimeField()
    details: LiteralString = models.TextField(max_length=500, null=False)
    link: LiteralString = models.CharField(max_length=50, null=False, default="https")

    def __str__(self) -> str:
        return self.name


class Certificates(models.Model):
    certificate_name: LiteralString = models.CharField(max_length=500)
    domain: LiteralString = models.CharField(max_length=500)
    file = models.FileField(upload_to='documents/%Y-%m-%d')
    certificate_issued_to = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.certificate_name
