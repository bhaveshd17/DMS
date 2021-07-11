from django.template.loader import render_to_string

from .models import *
import operator


def department_sort(request):
    roll_no = request.user.username
    student = Student.objects.get(roll_no=roll_no)
    branch = student.branch

    admin_int = AdminDma.objects.filter(department=branch)
    job_list = []
    int_list = []
    mock_list = []
    for admin in admin_int:
        jobs = Job.objects.filter(adm_id=admin.id)
        internships = Intership.objects.filter(adm_id=admin.id).order_by("apply_by")
        mockTests = Mock_test.objects.filter(adm_id=admin.id)
        for job in jobs:
            job_list.append(job)
        for internship in internships:
            int_list.append(internship)
        for mockTest in mockTests:
            mock_list.append(mockTest)

    return {'job_list': job_list, 'int_list': int_list, 'mock_list': mock_list}


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
        cgpa = CurrEdu.objects.get(roll_no_curr=student).average_sgpi
        live_kt = CurrEdu.objects.get(roll_no_curr=student).live_kt
        dead_kt = CurrEdu.objects.get(roll_no_curr=student).dead_kt
        drop = CurrEdu.objects.get(roll_no_curr=student).drop

        related_job_list = []
        hired = Job_user.objects.filter(roll_no=student, status="3")
        if len(hired) == 0:
            for job in job_list:
                if job.cgpa <= cgpa and int(live_kt) <= int(job.live_kt) and int(drop) <= int(job.drop) and int(
                        dead_kt) <= int(job.dead_kt):
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
                    if job.cgpa <= cgpa and int(live_kt) <= int(job.live_kt) and int(drop) <= int(
                            job.drop) and job.sal > 5:
                        related_job_list.append(job)
            elif sal > 7 and sal <= 10:
                for job in job_list:
                    if job.cgpa <= cgpa and int(live_kt) <= int(job.live_kt) and int(drop) <= int(
                            job.drop) and job.sal > 7:
                        related_job_list.append(job)
            elif sal > 10:
                for job in job_list:
                    if job.cgpa <= cgpa and int(live_kt) <= int(job.live_kt) and int(drop) <= int(
                            job.drop) and job.sal > 10:
                        related_job_list.append(job)
    except Exception as e:
        print(e)
        related_job_list = []

    # total avaialable skills
    skill_set = set()
    for job in job_list:
        job_split = job.skills.split(',')
        for i in job_split:
            skill_set.add(i.strip().upper())

    content = {'related_job_list': related_job_list,
               'skill_set': skill_set,
               'job_list': job_list1,
               'department_wise_job': job_list,
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

