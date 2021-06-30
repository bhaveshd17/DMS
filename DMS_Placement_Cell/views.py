from django.shortcuts import render
from .form import *

def index(request):
    content = {}
    return render(request, 'placement/index.html', content)

def add_intership(request):
    form=IntershipForm()
    content={"form":form}
    return render(request,"placement/add_intership.html",content)

def add_job(request):
    form=JobForm()
    content={"form":form}
    return render(request,"placement/add_job.html",content)