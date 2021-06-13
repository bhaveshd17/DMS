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
    int_obj = Intership.objects.all()
    content = {'int_obj':int_obj}
    return render(request, 'student/internship.html', content)

def preplacement(request):
    mock_test= Mock_test.objects.all()
    content = {'mock_test':mock_test}
    return render(request, 'student/preplacement.html', content)

def job(request):
    job_obj = Job.objects.all()
    content = {'job_obj':job_obj}
    return render(request, 'student/job.html', content)

def details(request,id,type):
    if type==1:
        job_obj = Job.objects.get(id=id)
        content={'details':job_obj}
    elif type==2:
        internship_obj = Intership.objects.get(id=id)
        content={'details':internship_obj}

    return render(request,"student/details.html",content)