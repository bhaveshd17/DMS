from django.template.loader import render_to_string

from .models import *
import operator
from .form import FeForm, SeForm, TeForm, BeForm

def branch_logic(rollNo):
    if rollNo[2:5]=="101":
        branch="INFT"
    elif rollNo[2:5]=="102":
        branch="CMPN"
    elif rollNo[2:5]=="103":
        branch="ETRX"
    elif rollNo[2:5]=="104":
        branch="EXTC"
    elif rollNo[2:5]=="105":
        branch="BIOMED"
    else:
        branch="Invalid User"
    return branch

def be_year_logic(request, year, pk=None, template_stat=None, csrf_token_value=None):
    form, obj, template = None, None, None
    if year == 'fe':
        form = FeForm(request.POST)
        if pk:
            obj = FE.objects.get(id=pk)
            form = FeForm(instance=obj)
            if request.method == 'POST':
                form = FeForm(request.POST, instance=obj)
            if template_stat:
                template = render_to_string('student/ajax_temp/curr_edu/fe.html',
                                            {'id': pk, 'csrf_token_value': csrf_token_value, 'form': form,
                                             'user': request.user})

    elif year == 'se':
        form = SeForm(request.POST)
        if pk:
            obj = SE.objects.get(id=pk)
            form = SeForm(instance=obj)
            if request.method == 'POST':
                form = SeForm(request.POST, instance=obj)
            if template_stat:
                template = render_to_string('student/ajax_temp/curr_edu/se.html',
                                            {'id': pk, 'csrf_token_value': csrf_token_value, 'form': form,
                                             'user': request.user})

    elif year == 'te':
        form = TeForm(request.POST)
        if pk:
            obj = TE.objects.get(id=pk)
            form = TeForm(instance=obj)
            if request.method == 'POST':
                form = TeForm(request.POST, instance=obj)

            if template_stat:
                template = render_to_string('student/ajax_temp/curr_edu/te.html',
                                            {'id': pk, 'csrf_token_value': csrf_token_value, 'form': form,
                                             'user': request.user})

    elif year == 'be':
        form = BeForm(request.POST)
        if pk:
            obj = BE.objects.get(id=pk)
            form = BeForm(instance=obj)
            if request.method == 'POST':
                form = BeForm(request.POST, instance=obj)
            if template_stat:
                template = render_to_string('student/ajax_temp/curr_edu/be.html',
                                            {'id': pk, 'csrf_token_value': csrf_token_value, 'form': form,
                                             'user': request.user})

    return {'form':form, 'del_obj':obj, 'template':template}



def department_sort(request):
    roll_no = request.user.username
    branch = branch_logic(roll_no)

    admin_int = AdminDma.objects.filter(department=branch)
    job_list = []
    int_list = []
    mock_list = []
    for admin in admin_int:
        jobs = Job.objects.filter(adm_id=admin.id)
        internships = Intership.objects.filter(adm_id=admin.id).order_by("apply_by")
        mockTests= Mock_test.objects.filter(adm_id=admin.id)
        for job in jobs:
            job_list.append(job)
        for internship in internships:
            int_list.append(internship)
        for mockTest in mockTests:
            mock_list.append(mockTest)

    return {'job_list':job_list, 'int_list':int_list, 'mock_list':mock_list}

def jobLogic(request):
    job_list1 = department_sort(request)['job_list']
    student = Student.objects.get(roll_no=request.user.username)
    student_skills = student.skills
    student_skills_split = student_skills.split(',')
    student_skills_list = []
    for skills in student_skills_split:
        student_skills_list.append(skills.strip().lower())

    # job logic
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
        cgpa = BE.objects.get(roll_no_4=student).be_cgpa
        live_kt = BE.objects.get(roll_no_4=student).kt_BE
        drop_2 = SE.objects.get(roll_no_2=student).drop_SE
        drop_3 = TE.objects.get(roll_no_3=student).drop_TE
        drop_4 = BE.objects.get(roll_no_4=student).drop_BE
        drop = int(drop_2) + int(drop_3) + int(drop_4)
        related_job_list = []

        hired = Job_user.objects.filter(roll_no=student, status="3")
        if len(hired) ==0:
            for job in job_list:
                if job.cgpa <= cgpa and int(live_kt) <= int(job.live_kt) and int(drop) <= int(job.drop):
                    related_job_list.append(job)
        else:
            package = []
            for job in hired:
                package.append(Job.objects.get(id=job.job_id.id).sal)

            sal = max(package)
            if sal < 3.5:
                for job in job_list:
                    if job.cgpa <= cgpa and int(live_kt) <= int(job.live_kt) and int(drop) <= int(job.drop):
                        related_job_list.append(job)
            elif sal >= 3.5 and sal <= 5:
                for job in job_list:
                    if job.cgpa <= cgpa and int(live_kt) <= int(job.live_kt) and int(drop) <= int(
                            job.drop) and job.sal >= 5:
                        related_job_list.append(job)
            elif sal > 5 and sal <= 7:
                for job in job_list:
                    if job.cgpa <= cgpa and int(live_kt) <= int(job.live_kt) and int(drop) <= int(job.drop) and job.sal > 5:
                        related_job_list.append(job)
            elif sal > 7 and sal <= 10:
                for job in job_list:
                    if job.cgpa <= cgpa and int(live_kt) <= int(job.live_kt) and int(drop) <= int(job.drop) and job.sal > 7:
                        related_job_list.append(job)
            elif sal > 10:
                for job in job_list:
                    if job.cgpa <= cgpa and int(live_kt) <= int(job.live_kt) and int(drop) <= int(
                            job.drop) and job.sal > 10:
                        related_job_list.append(job)
    except:
        related_job_list = []


    #total avaialable skills
    skill_set = set()
    for job in job_list:
        job_split = job.skills.split(',')
        for i in job_split:
            skill_set.add(i.strip().upper())



    content = {'related_job_list': related_job_list,
               'skill_set':skill_set,
               'job_list':job_list1
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
        'skill_set':skill_set,
        'int_list':int_list
    }