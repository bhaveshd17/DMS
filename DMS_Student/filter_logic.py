from .models import Job, Student
from .utils import internshipLogic, department_sort, jobLogic
from datetime import datetime
from typing import List, Dict, Any, TypedDict, LiteralString

class InternshipData(TypedDict):
    related_int_list: List[Any]
    int_list: List[Any]

class JobData(TypedDict):
    related_job_list: List[Any]

def intern_filters(request: Any) -> Dict[str, Any]:
    data: InternshipData = internshipLogic(request)
    internship = data['related_int_list']
    skills: List[LiteralString] = request.GET.getlist('skills[]')
    duration: List[LiteralString] = request.GET.getlist('duration[]')
    stipend: LiteralString = request.GET.get('stipend')
    starting_from: LiteralString = request.GET.get('starting_from')
    sort_by_date: LiteralString = request.GET.get('sort_by_date')
    work_from_home: LiteralString = request.GET.get('work_from_home')

    if sort_by_date == 'true':
        int_list = data.get('int_list', [])
        internship = int_list

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
        try:
            start_date = datetime.strptime(starting_from, "%Y-%m-%d").date()
        except ValueError as e:
            e.add_note(f"Invalid date format for starting_from: {starting_from}. Expected format: YYYY-MM-DD.")
            raise
        for int_obj in internship:
            if int_obj.start_date >= start_date:
                temp_list.append(int_obj)
        internship = temp_list

    if work_from_home == "true":
        temp_list = []
        for int_obj in internship:
            if int_obj.work_from_home:
                temp_list.append(int_obj)
        internship = temp_list

    return {'internship': internship, 'data': data}

def job_filters(request: Any) -> Dict[str, Any]:
    data: JobData = jobLogic(request)
    url_path: LiteralString = request.GET.get('path')
    if "all_job" in url_path:
        job = Job.objects.filter(year=Student.objects.get(roll_no=request.user.username).year_of_graduation)
    else:
        job = data['related_job_list']
    skills: List[LiteralString] = request.GET.getlist('skills[]')
    salary: LiteralString = request.GET.get('salary')
    location: List[LiteralString] = request.GET.getlist('location[]')
    sort_by_date: LiteralString = request.GET.get('sort_by_date')
    work_from_home: LiteralString = request.GET.get('work_from_home')

    if sort_by_date == 'true':
        if "all_job" in url_path:
            job = Job.objects.filter(year=Student.objects.get(roll_no=request.user.username).year_of_graduation).order_by("-apply_by")
        else:
            job = data['related_job_list']

    if skills[0] != 'e.g. JAVA':
        temp_list = []
        for job_obj in job:
            job_split = job_obj.skills.split(',')
            for j in job_split:
                if j.strip().lower() == skills[0].lower():
                    temp_list.append(job_obj)
        job = temp_list

    if salary != '0':
        temp_list = []
        for job_obj in job:
            sal = job_obj.sal.split(',')
            for s in sal:
                if float(s) >= float(salary) * 100000 * 2:
                    temp_list.append(job_obj)

        temp_list.sort(key=lambda x: x.sal)
        job = temp_list

    if location[0] != "e.g. Mumbai":
        temp_list = []
        for job_obj in job:
            if job_obj.location.lower() == location[0].lower():
                temp_list.append(job_obj)
        job = temp_list

    if work_from_home == "true":
        temp_list = []
        for job_obj in job:
            if job_obj.work_from_home:
                temp_list.append(job_obj)
        job = temp_list

    return {'job': job, 'data': data}
