from django.shortcuts import render
from .models import *

def index(request):
    # job_obj = job()
    content = {}
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

