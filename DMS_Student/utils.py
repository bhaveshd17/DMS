from django.template.loader import render_to_string
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.conf import settings
from django.db.models import Max

import six
from .models import *
import operator
import numpy as np
import math


def job_eligibility_logic(job_list, percentage, live_kt, drop, dead_kt, ssc_percentage, hsc_percentage, sal):
    list_j = []
    for job in job_list:
        salary = job.sal.split(',')
        for s in salary:
            if float(job.aggregate_sgpi) <= percentage and float(job.ssc_percentage) <= ssc_percentage and float(
                job.hsc_d_percentage) <= hsc_percentage and live_kt <= int(job.live_kt) and drop <= int(job.drop) and dead_kt <= int(job.dead_kt) and float(s) > sal:
                list_j.append(job)
    return list_j


def department_sort(request):
    roll_no = request.user.username
    student = Student.objects.get(roll_no=roll_no)
    branch = student.branch
    jobs = Job.objects.filter(recruiting_from__icontains=branch)
    internships = Intership.objects.all()
    mockTests = Mock_test.objects.all()


    return {'job_list': jobs, 'int_list': internships, 'mock_list': mockTests}



def jobLogic(request):
    job_list1 = department_sort(request)['job_list']
    student = Student.objects.get(roll_no=request.user.username)
    student_skills = student.skills
    student_skills_split = student_skills.split(',')
    student_skills_list = []
    for skills in student_skills_split:
        student_skills_list.append(skills.strip().lower())

    # job logic
    related_job_list = []
    related_jobs = {}
    for job_obj in job_list1:
        count = 0
        job_split = job_obj.skills.split(',')
        for skills in student_skills_list:
            for job in job_split:
                if job.strip().lower() == skills:
                    count = count + 1

        score = (count * 100) / len(job_split)

        related_jobs[job_obj.id] = score

    sorted_related_jobs = dict(sorted(related_jobs.items(), key=operator.itemgetter(1), reverse=True))

    job_list = []
    for id in sorted_related_jobs.keys():
        job_list.append(Job.objects.get(id=id))

    try:
        student = Student.objects.get(roll_no=request.user.username)
        curr_edu = CurrEdu.objects.get(roll_no_curr=student)
        cgpa = float(curr_edu.average_sgpi)
        percentage = float(round(cgpa * 7.1 + 11, 2))
        live_kt = int(curr_edu.live_kt)
        dead_kt = int(curr_edu.dead_kt)
        drop = int(curr_edu.drop)
        ssc = Add_edu.objects.get(roll_no=student, degree='10')
        ssc_percentage = round(ssc.marks / int(ssc.no_of_subject), 2)
        hsc = Add_edu.objects.filter(roll_no=student).exclude(degree='10')[0]
        if hsc.degree == 'diploma':
            hsc_percentage = hsc.percentage
        else:
            hsc_percentage = round(hsc.marks / int(hsc.no_of_subject))

        hired = Job_user.objects.filter(roll_no=student, status="3")
        if curr_edu.sgpi5 == "NA":
            related_job_list = []
        else:
            if len(hired) == 0:
                related_job_list = job_eligibility_logic(job_list=job_list, percentage=percentage,
                                                         live_kt=live_kt, dead_kt=dead_kt, drop=drop,
                                                         ssc_percentage=ssc_percentage, hsc_percentage=hsc_percentage,
                                                         sal=0)

            else:
                package = []
                for job in hired:
                    package.append(Job.objects.get(id=job.job_id.id).sal)
                sal = max(package)

                if sal < 3.0:
                    related_job_list = job_eligibility_logic(job_list=job_list, percentage=percentage,
                                                             live_kt=live_kt, dead_kt=dead_kt, drop=drop,
                                                             ssc_percentage=ssc_percentage,
                                                             hsc_percentage=hsc_percentage,
                                                             sal=3.0)
                else:
                    max_package = Job.objects.aggregate(Max('sal'))['sal__max']
                    linear_space_package = np.linspace(start=3.0, stop=max_package, num=int(max_package / 2))
                    arranging = zip(linear_space_package, linear_space_package[1:])
                    for i, j in arranging:
                        if sal >= float(math.ceil(i)) and sal < float(math.ceil(j)):
                            related_job_list = job_eligibility_logic(job_list=job_list, percentage=percentage,
                                                                     live_kt=live_kt, dead_kt=dead_kt, drop=drop,
                                                                     ssc_percentage=ssc_percentage,
                                                                     hsc_percentage=hsc_percentage,
                                                                     sal=j)

    except Exception as e:
        print(e)
        related_job_list = []

    # total avaialable skills
    skill_set = set()
    for job in job_list:
        job_split = job.skills.split(',')
        for i in job_split:
            skill_set.add(i.strip().upper())

    cities = set()
    for job in job_list:
        cities.add(job.location)

    content = {'related_job_list': related_job_list,
               'skill_set': skill_set,
               'job_list': job_list1,
               'department_wise_job_skill_based': job_list,
               'cities': cities,
               }
    return content


def internshipLogic(request):
    student = Student.objects.get(roll_no=request.user.username)
    student_skills = student.skills
    student_skills_split = student_skills.split(',')
    student_skills_list = []
    for skills in student_skills_split:
        student_skills_list.append(skills.strip().lower())

    int_list = department_sort(request)['int_list']
    # internship logic

    related_internship = {}
    for int_obj in int_list:
        count = 0
        int_split = int_obj.skills.split(',')
        for skills in student_skills_list:
            for intern in int_split:
                if intern.strip().lower() == skills:
                    count = count + 1

        score = (count * 100) / len(int_split)

        related_internship[int_obj.id] = score

    sorted_related_int = dict(sorted(related_internship.items(), key=operator.itemgetter(1), reverse=True))
    related_int_list = []
    for id in sorted_related_int.keys():
        related_int_list.append(Intership.objects.get(id=id))

    skill_set = set()
    for intern in int_list:
        intern_split = intern.skills.split(',')
        for i in intern_split:
            skill_set.add(i.strip().upper())

    return {
        'related_int_list': related_int_list,
        'skill_set': skill_set,
        'int_list': int_list
    }


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, student, timestamp):
        return (six.text_type(student.roll_no) + six.text_type(timestamp) + six.text_type(student.is_email_verified))


generate_token = TokenGenerator()


def send_action_email(student, name, request):
    current_site = get_current_site(request)
    email_subject = "Activate your VPlacement Portal"
    email_body = render_to_string("authentication/activate.html", {
        'student': student,
        'name': name,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(student.roll_no)),
        'token': generate_token.make_token(student)

    })

    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email=settings.EMAIL_HOST_USER,
                         to=[student.gmail]
                         )
    email.fail_silently = False
    email.content_subtype = 'html'
    email.send()


def forgot_password_email(student, request):
    current_site = get_current_site(request)
    email_subject = "Forgot Password"
    email_body = render_to_string("authentication/forgot_password_email.html", {
        'student': student,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(student.roll_no)),
    })

    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email=settings.EMAIL_HOST_USER,
                         to=[student.gmail]
                         )
    email.fail_silently = False
    email.content_subtype = 'html'
    email.send()