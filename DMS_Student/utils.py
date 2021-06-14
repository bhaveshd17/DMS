from .models import *
import operator

def IntershipJobLogic(request):
    roll_no = request.user.username
    if roll_no[2:5] == "101":
        branch = "INFT"
    elif roll_no[2:5] == "102":
        branch = "CMPN"
    elif roll_no[2:5] == "103":
        branch = "ETRX"
    elif roll_no[2:5] == "104":
        branch = "EXTC"
    elif roll_no[2:5] == "105":
        branch = "BIOMED"
    else:
        branch = "Invalid User"


    admin_int = AdminDma.objects.filter(department=branch)
    job_list = []
    int_list = []
    mock_list = []
    for admin in admin_int:
        jobs = Job.objects.filter(adm_id=admin.id)
        internships = Intership.objects.filter(adm_id=admin.id)
        mockTests= Mock_test.objects.filter(adm_id=admin.id)
        for job in jobs:
            job_list.append(job)
        for internship in internships:
            int_list.append(internship)
        for mockTest in mockTests:
            mock_list.append(mockTest)


    student = Student.objects.get(roll_no=roll_no)
    student_skills = student.skills
    student_skills_split = student_skills.split(',')
    student_skills_list = []
    for skills in student_skills_split:
        student_skills_list.append(skills.strip().lower())

    # job logic

    related_jobs = {}
    for job_obj in job_list:
        count = 0
        job_split = job_obj.skills.split(',')
        for skills in student_skills_list:
            for job in job_split:
                if job.strip().lower() == skills:
                    count = count + 1

        score = (count * 100) / len(job_split)

        related_jobs[job_obj.id] = score

    sorted_related_jobs = dict(sorted(related_jobs.items(), key=operator.itemgetter(1), reverse=True))

    related_job_list = []
    for id in sorted_related_jobs.keys():
        related_job_list.append(Job.objects.get(id=id))

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


    content = {'related_job_list': related_job_list,
               'related_int_list': related_int_list,
               'mock_list':mock_list}
    return content