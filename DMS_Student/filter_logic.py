from .utils import IntershipJobLogic
from datetime import datetime


def intern_filters(request):
    data = IntershipJobLogic(request)
    internship = data['related_int_list']
    skills = request.GET.getlist('skills[]')
    duration = request.GET.getlist('duration[]')
    stipend = request.GET.get('stipend')
    starting_from = request.GET.get('starting_from')
    sort_by_date = request.GET.get('sort_by_date')

    if skills[0] != 'e.g. JAVA':
        temp_list = []
        for int_obj in internship:
            int_split = int_obj.skills.split(',')
            for intern in int_split:
                if intern.strip().lower() == skills[0].lower():
                    temp_list.append(int_obj)
        internship = temp_list

    if stipend != '0':
        temp_list = []
        for int_obj in internship:
            if int_obj.sal >= int(stipend) * 2 * 1000:
                temp_list.append(int_obj)
        temp_list.sort(key=lambda x: x.sal)

        internship = temp_list

    if duration[0] != 'choose duration':
        temp_list = []
        for int_obj in internship:
            if duration[0] in int_obj.duration:
                temp_list.append(int_obj)
        internship = temp_list

    if starting_from != '':
        temp_list = []
        for int_obj in internship:
            if int_obj.start_date >= datetime.strptime(starting_from, "%Y-%m-%d").date():
                temp_list.append(int_obj)
        internship = temp_list

    if sort_by_date == 'true':
        int_list = data['int_list']
        internship = int_list

    return {'internship':internship, 'data':data}


def job_filters(request):
    data = IntershipJobLogic(request)
    job = data['related_job_list']
    skills = request.GET.getlist('skills[]')
    salary = request.GET.get('salary')
    location = request.GET.getlist('location[]')
    starting_from = request.GET.get('starting_from')
    sort_by_date = request.GET.get('sort_by_date')


    if skills[0] != 'e.g. JAVA':
        temp_list = []
        for job_obj in job:
            job_split = job_obj.skills.split(',')
            for j in job_split:
                if j.strip().lower() == skills[0].lower():
                    temp_list.append(job_obj)
        job = temp_list

    if salary != '3':
        temp_list = []
        for job_obj in job:
            if job_obj.sal >= int(salary) * 3:
                temp_list.append(job_obj)
        temp_list.sort(key=lambda x: x.sal)

        job = temp_list

    if location[0] != "e.g. Mumbai":
        temp_list = []
        for job_obj in job:
            if job_obj.location.lower() == location[0].lower():
                temp_list.append(job_obj)
        job = temp_list


    if starting_from != '':
        temp_list = []
        for job_obj in job:
            if job_obj.start_date >= datetime.strptime(starting_from, "%Y-%m-%d").date():
                temp_list.append(job_obj)
        job = temp_list


    if sort_by_date == 'true':
        job_list = data['job_list']
        job = job_list

    return {'job':job, 'data':data}