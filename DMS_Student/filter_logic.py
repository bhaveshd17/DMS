from .models import Job, Student
from .utils import internshipLogic, department_sort, jobLogic
from datetime import datetime
from typing import List, Dict, Any, TypedDict, LiteralString
from dataclasses import dataclass

class InternshipData(TypedDict):
    related_int_list: List[Any]
    int_list: List[Any]

class JobData(TypedDict):
    related_job_list: List[Any]

@dataclass
class InternshipFilterParams:
    skills: List[LiteralString]
    duration: List[LiteralString]
    stipend: LiteralString
    starting_from: LiteralString
    sort_by_date: LiteralString
    work_from_home: LiteralString

@dataclass
class JobFilterParams:
    skills: List[LiteralString]
    salary: LiteralString
    location: List[LiteralString]
    sort_by_date: LiteralString
    work_from_home: LiteralString

def intern_filters(request: Any) -> Dict[str, Any]:
    data: InternshipData = internshipLogic(request)
    internship = data['related_int_list']
    params = InternshipFilterParams(
        skills=request.GET.getlist('skills[]'),
        duration=request.GET.getlist('duration[]'),
        stipend=request.GET.get('stipend'),
        starting_from=request.GET.get('starting_from'),
        sort_by_date=request.GET.get('sort_by_date'),
        work_from_home=request.GET.get('work_from_home')
    )

    if params.sort_by_date == 'true':
        int_list = data.get('int_list', [])
        internship = int_list

    if params.skills[0] != 'e.g. JAVA':
        temp_list = []
        for int_obj in internship:
            int_split = int_obj.skills.split(',')
            for intern in int_split:
                if intern.strip().lower() == params.skills[0].lower():
                    temp_list.append(int_obj)
        internship = temp_list

    if params.stipend != '0':
        temp_list = []
        for int_obj in internship:
            if int_obj.sal >= int(params.stipend) * 2 * 1000:
                temp_list.append(int_obj)
        temp_list.sort(key=lambda x: x.sal)

        internship = temp_list

    if params.duration[0] != 'choose duration':
        temp_list = []
        for int_obj in internship:
            if params.duration[0] in int_obj.duration:
                temp_list.append(int_obj)
        internship = temp_list

    if params.starting_from != '':
        temp_list = []
        try:
            start_date = datetime.strptime(params.starting_from, "%Y-%m-%d").date()
        except ValueError as e:
            e.add_note(f"Invalid date format for starting_from: {params.starting_from}. Expected format: YYYY-MM-DD.")
            raise
        for int_obj in internship:
            if int_obj.start_date >= start_date:
                temp_list.append(int_obj)
        internship = temp_list

    if params.work_from_home == "true":
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
    
    params = JobFilterParams(
        skills=request.GET.getlist('skills[]'),
        salary=request.GET.get('salary'),
        location=request.GET.getlist('location[]'),
        sort_by_date=request.GET.get('sort_by_date'),
        work_from_home=request.GET.get('work_from_home')
    )

    if params.sort_by_date == 'true':
        if "all_job" in url_path:
            job = Job.objects.filter(year=Student.objects.get(roll_no=request.user.username).year_of_graduation).order_by("-apply_by")
        else:
            job = data['related_job_list']

    if params.skills[0] != 'e.g. JAVA':
        temp_list = []
        for job_obj in job:
            job_split = job_obj.skills.split(',')
            for j in job_split:
                if j.strip().lower() == params.skills[0].lower():
                    temp_list.append(job_obj)
        job = temp_list

    if params.salary != '0':
        temp_list = []
        for job_obj in job:
            sal = job_obj.sal.split(',')
            for s in sal:
                if float(s) >= float(params.salary) * 100000 * 2:
                    temp_list.append(job_obj)

        temp_list.sort(key=lambda x: x.sal)
        job = temp_list

    if params.location[0] != "e.g. Mumbai":
        temp_list = []
        for job_obj in job:
            if job_obj.location.lower() == params.location[0].lower():
                temp_list.append(job_obj)
        job = temp_list

    if params.work_from_home == "true":
        temp_list = []
        for job_obj in job:
            if job_obj.work_from_home:
                temp_list.append(job_obj)
        job = temp_list

    return {'job': job, 'data': data}
