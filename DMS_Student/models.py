from django.db import models
from django.core.validators import MaxValueValidator
from typing import Annotated


class Student(models.Model):
    roll_no: Annotated[str, models.CharField(primary_key=True, max_length=20, null=False)]
    phone: Annotated[str, models.CharField(max_length=10, null=True)]
    skills: Annotated[str, models.TextField(max_length=500, null=False)]
    age = models.IntegerField(validators=[MaxValueValidator(99)], null=True)
    gender: Annotated[str, models.CharField(max_length=15, choices=sorted({
        ("Male", "Male"), ("Female", "Female"), ("Other", "Other")
    }), null=True)]
    branch: Annotated[str, models.CharField(max_length=12, choices=sorted({
        ("INFT", "INFT"), ("CMPN", "CMPN"), ("EXTC", "EXTC"), ("ETRX", "ETRX"), ("BIOM", "BIOM")
    }), null=True)]
    div: Annotated[str, models.CharField(max_length=12, choices=sorted({
        ("A", "A"), ("B", "B"), ("C", "C")
    }), null=True)]
    corresponding_address: Annotated[str, models.TextField(max_length=500, null=True)]
    permanent_address: Annotated[str, models.TextField(max_length=500, null=True)]
    date_of_birth = models.DateField(null=True)
    gmail = models.EmailField(null=True)
    residence_phone: Annotated[str, models.CharField(max_length=10, null=True)]
    pan_card_no: Annotated[str, models.CharField(max_length=10, null=True)]
    aadhar_no: Annotated[str, models.CharField(max_length=12, null=True)]
    passport_no: Annotated[str, models.CharField(max_length=9, null=True)]
    year_of_graduation = models.IntegerField(null=True, db_index=True)
    disability = models.BooleanField(null=True)
    type_of_disability: Annotated[str, models.CharField(max_length=100, null=True)]
    father_name: Annotated[str, models.CharField(max_length=50, null=True)]
    mother_name: Annotated[str, models.CharField(max_length=50, null=True)]
    father_occupation: Annotated[str, models.CharField(max_length=50, null=True)]
    mother_occupation: Annotated[str, models.CharField(max_length=50, null=True)]
    co_curriculum_activities: Annotated[str, models.CharField(max_length=100, null=True)]
    extra_curriculum_activities: Annotated[str, models.CharField(max_length=100, null=True)]
    hobbies: Annotated[str, models.CharField(max_length=150, null=True)]
    profile_photo = models.ImageField(upload_to="profile/", null=True)
    resume = models.FileField(upload_to="Resume/", null=True)
    facebook = models.URLField(null=True)
    linkdin = models.URLField(null=True)
    github = models.URLField(null=True)
    other: Annotated[str, models.CharField(max_length=150, null=True)]
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
    clg_name: Annotated[str, models.CharField(max_length=50, null=False)]
    degree: Annotated[str, models.CharField(max_length=50, choices=degree_choice, null=True)]
    no_of_subject: Annotated[str, models.CharField(max_length=20, null=True)]
    board: Annotated[str, models.CharField(max_length=50, null=True)]
    percentage = models.FloatField(null=False)
    start_year = models.DateField(null=False)
    end_year = models.DateField(null=False)
    marks = models.IntegerField(validators=[MaxValueValidator(999)])
    roll_no = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    gap: Annotated[str, models.CharField(max_length=15, choices=sorted({
        ("0", "0 year"), ("1", "1 year"), ("2", "2 years"), ("3", "3 years"), ("4", "4 years"), ("5", "5 years")
    }), null=True)]

    diploma_pattern: Annotated[str, models.CharField(max_length=20, choices={
        ("semester pattern", "semester pattern"), ("yearly pattern", "yearly pattern"), ("NA", "NA")
    }, default="NA")]
    diploma_aggregate_mw: Annotated[str, models.CharField(max_length=100, default="NA")]
    diploma_aggregate_pw: Annotated[str, models.CharField(max_length=100, default="NA")]
    no_of_dead_kt: Annotated[str, models.CharField(max_length=10, default="NA")]

    def __str__(self) -> str:
        return self.clg_name


class Add_exp(models.Model):
    comp_name: Annotated[str, models.CharField(max_length=50, null=False)]
    role: Annotated[str, models.CharField(max_length=50, null=False)]
    duration: Annotated[str, models.CharField(max_length=50, null=False)]
    rollNo = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    start_date = models.DateField(null=False)

    def __str__(self) -> str:
        return self.comp_name


class CurrEdu(models.Model):
    roll_no_curr = models.ForeignKey(Student, on_delete=models.CASCADE)
    sgpi1: Annotated[str, models.CharField(max_length=4, default="NA")]
    sgpi2: Annotated[str, models.CharField(max_length=4, default="NA")]
    cgpa1: Annotated[str, models.CharField(max_length=4, default="NA")]
    sgpi3: Annotated[str, models.CharField(max_length=4, default="NA")]
    sgpi4: Annotated[str, models.CharField(max_length=4, default="NA")]
    cgpa2: Annotated[str, models.CharField(max_length=4, default="NA")]
    sgpi5: Annotated[str, models.CharField(max_length=4, default="NA")]
    sgpi6: Annotated[str, models.CharField(max_length=4, default="NA")]
    cgpa3: Annotated[str, models.CharField(max_length=4, default="NA")]
    sgpi7: Annotated[str, models.CharField(max_length=4, default="NA")]
    sgpi8: Annotated[str, models.CharField(max_length=4, default="NA")]
    cgpa4: Annotated[str, models.CharField(max_length=4, default="NA")]
    live_kt: Annotated[str, models.CharField(max_length=15, null=True)]
    dead_kt: Annotated[str, models.CharField(max_length=15, null=True)]
    drop: Annotated[str, models.CharField(max_length=15, choices=sorted({
        ("0", "0 year"), ("1", "1 year"), ("2", "2 years"), ("3", "3 years"), ("4", "4 years"), ("5", "5 years")
    }), null=True)]
    total_grade = models.FloatField(validators=[MaxValueValidator(100)], null=True, default=0)
    average_sgpi = models.FloatField(validators=[MaxValueValidator(10)], null=True, default=0)

    def __str__(self) -> str:
        return str(self.roll_no_curr)


class Intership(models.Model):
    comp_name: Annotated[str, models.CharField(max_length=40, null=False)]
    link: Annotated[str, models.CharField(max_length=150, null=False)]
    start_date = models.DateField(null=False)
    apply_by = models.DateField(null=False)
    sal = models.IntegerField(null=False)
    skills: Annotated[str, models.TextField(max_length=500, null=False)]
    duration: Annotated[str, models.CharField(max_length=20, null=False)]
    domain: Annotated[str, models.CharField(max_length=100, null=False)]
    about_comp: Annotated[str, models.TextField(max_length=500, null=False)]
    about_work: Annotated[str, models.TextField(max_length=500, null=False)]
    who_can_apply: Annotated[str, models.TextField(max_length=500, null=False)]
    perks: Annotated[str, models.TextField(max_length=500, null=False)]
    additional: Annotated[str, models.TextField(max_length=500, null=False)]
    work_from_home = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.comp_name


class Int_user(models.Model):
    status: Annotated[str, models.CharField(max_length=10, null=False)]
    roll_no = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    int_id = models.ForeignKey(Intership, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return str(self.roll_no)


class Job(models.Model):
    comp_name: Annotated[str, models.CharField(max_length=40, null=False)]
    location: Annotated[str, models.CharField(max_length=100)]
    recruiting_from: Annotated[str, models.CharField(max_length=500, null=True, default="NA")]
    link: Annotated[str, models.CharField(max_length=150, null=False)]
    year: Annotated[str, models.CharField(max_length=25, null=True, blank=True)]
    apply_by = models.DateField(null=True)
    sal: Annotated[str, models.CharField(null=False, max_length=150)]
    skills: Annotated[str, models.TextField(max_length=500, null=False)]
    domain: Annotated[str, models.CharField(max_length=100, choices=sorted({
        ("Automotive", "Automotive"), ("Banking", "Banking"), ("EduTech", "EduTech"), ("Financial Services", "Financial Services"),
        ("Information Technology", "Information Technology"), ("Logistics & Supply Chain", "Logistics & Supply Chain"),
        ("Retail", "Retail"), ("Telecommunications", "Telecommunications"), ("Electrical Manufacturing", "Electrical Manufacturing"),
        ("Marketing & Advertising", "Marketing & Advertising"), ("Media Production", "Media Production"),
        ("Management Consulting", "Management Consulting"), ("Manufacturing", "Manufacturing"), ("Health Care", "Health Care"),
        ("Design", "Design"), ("Professional Services", "Professional Services")
    }))]
    about_comp: Annotated[str, models.TextField(max_length=500, null=False)]
    about_work: Annotated[str, models.TextField(max_length=500, null=False)]
    aggregate_sgpi: Annotated[str, models.CharField(max_length=15, null=True)]
    ssc_percentage: Annotated[str, models.CharField(max_length=15, null=True)]
    hsc_d_percentage: Annotated[str, models.CharField(max_length=15, null=True)]
    live_kt: Annotated[str, models.CharField(max_length=15, null=True)]
    dead_kt: Annotated[str, models.CharField(max_length=15, null=True)]
    drop: Annotated[str, models.CharField(max_length=15, choices=sorted({
        ("0", "0 year"), ("1", "1 year"), ("2", "2 years"), ("3", "3 years"), ("4", "4 years"), ("5", "5 years")
    }), null=True)]
    who_can_apply: Annotated[str, models.TextField(max_length=500, null=True, blank=True)]
    perks: Annotated[str, models.TextField(max_length=500, null=False)]
    additional: Annotated[str, models.TextField(max_length=500, null=False)]
    status: Annotated[str, models.CharField(max_length=10, null=True, default=0)]
    work_from_home = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.comp_name


class Job_user(models.Model):
    status: Annotated[str, models.CharField(max_length=10, null=False)]
    roll_no = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now_add=True, null=True)
    salary: Annotated[str, models.CharField(max_length=50, null=True)]
    is_mail_send = models.BooleanField(default=False, null=True)

    def __str__(self) -> str:
        return str(self.roll_no) + "," + str(self.job_id)


class Mock_test(models.Model):
    name: Annotated[str, models.CharField(max_length=30, null=True)]
    date = models.DateField(null=False)
    from_time = models.TimeField()
    to_time = models.TimeField()
    details: Annotated[str, models.TextField(max_length=500, null=False)]
    link: Annotated[str, models.CharField(max_length=50, null=False, default="https")]

    def __str__(self) -> str:
        return self.name


class Certificates(models.Model):
    certificate_name: Annotated[str, models.CharField(max_length=500)]
    domain: Annotated[str, models.CharField(max_length=500)]
    file = models.FileField(upload_to='documents/%Y-%m-%d')
    certificate_issued_to = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.certificate_name
