from DMS_Student.views import apply
from django.contrib import messages
from django.shortcuts import redirect, render
from .form import *
from DMS_Student.decorators import allowed_users
from DMS_Student.models import *
from datetime import date

@allowed_users(allowed_roles=['Placement_Cell'])
def index(request):
    int_user = Int_user.objects.all().order_by("id")
    job_user = Job_user.objects.all().order_by("id")
    content = {'int_user':int_user, 'job_user':job_user}
    return render(request, 'placement/index.html', content)

@allowed_users(allowed_roles=['Placement_Cell'])
def add_intership(request):
    form=IntershipForm()
    id=AdminDma.objects.get(name=request.user.username).id
    content={"form":form,"id":id}
    return render(request,"placement/add_intership.html",content)

@allowed_users(allowed_roles=['Placement_Cell'])
def add_job(request):
    form=JobForm()
    id=AdminDma.objects.get(name=request.user.username).id
    content={"form":form,"id":id}
    return render(request,"placement/add_job.html",content)

@allowed_users(allowed_roles=['Placement_Cell'])
def form_intership(request):
    if request.method=="POST":
        form=IntershipForm(request.POST)
        if form.is_valid():
            # print(form)
            form.save()
            messages.success(request,"Internship Added Successfully.")
            return redirect("placementIndex")
    return redirect("add_intership")

@allowed_users(allowed_roles=['Placement_Cell'])
def form_job(request):
    if request.method=="POST":
        form=JobForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Job Added Successfully.")
            return redirect("placementIndex")
    return redirect("add_job")

@allowed_users(allowed_roles=['Placement_Cell'])
def recruiting(request):
    jobs=Job.objects.filter(status=0)
    curr=Job.objects.filter(status=0,apply_by__gt=date.today())
    print(curr)
    context={"jobs":jobs}
    return render(request,"placement/recruiting.html",context)

@allowed_users(allowed_roles=['Placement_Cell'])
def recruited(request):
    jobs=Job.objects.filter(status=1)
    placed=Job_user.objects.filter(status=3)
    hired={}
    for job in jobs:
        count=0
        for p in placed:
            print(p.job_id,job)
            if p.job_id==job:
                count+=1
        hired[job]=count
    print(type(jobs),type(hired))
    context={"jobs":jobs,"hired":hired}
    return render(request,"placement/recruited.html",context)