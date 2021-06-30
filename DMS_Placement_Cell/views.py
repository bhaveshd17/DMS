from django.shortcuts import render
from .form import *
from DMS_Student.decorators import allowed_users
from DMS_Student.models import *

@allowed_users(allowed_roles=['Placement_Cell'])
def index(request):
    int_user = Int_user.objects.all().order_by("id")
    job_user = Job_user.objects.all().order_by("id")
    content = {'int_user':int_user, 'job_user':job_user}
    return render(request, 'placement/index.html', content)

@allowed_users(allowed_roles=['Placement_Cell'])
def add_intership(request):
    form=IntershipForm()
    content={"form":form}
    return render(request,"placement/add_intership.html",content)

@allowed_users(allowed_roles=['Placement_Cell'])
def add_job(request):
    form=JobForm()
    content={"form":form}
    return render(request,"placement/add_job.html",content)


