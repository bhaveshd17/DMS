from django.shortcuts import render
from .models import *
def index(request):
    job_obj = Job.objects.all()
    job_list = []
    for job in job_obj:
        job_list.append(job)

    int_obj = Intership.objects.all()
    int_list = []
    for intern in int_obj:
        int_list.append(intern)
    
    content = {'job_list':job_list[:3], 'int_list': int_list[:3]}
    return render(request, 'student/index.html', content)

def internship(request):
    content = {}
    return render(request, 'student/internship.html', content)

def preplacement(request):
    content = {}
    return render(request, 'student/preplacement.html', content)

def job(request):
    content = {}
    return render(request, 'student/job.html', content)

