from django.http import JsonResponse
from DMS_Student.views import apply
from django.contrib import messages
from django.shortcuts import redirect, render
from .form import *
from DMS_Student.decorators import allowed_users
from DMS_Student.models import *
from datetime import date
from django.contrib.auth.models import User
import json
from .utils import *

@allowed_users(allowed_roles=['Placement_Cell'])
def index(request):
    int_user = Int_user.objects.all().order_by("int_id__comp_name")
    job_user = Job_user.objects.all().order_by("job_id__comp_name")
    total_student=Student.objects.all().count()
    total_placed=Job_user.objects.filter(status="3").distinct().count()
    highest=Job_user.objects.filter(status="3")
    package=[]
    for job in highest:
        package.append(Job.objects.get(id=job.job_id.id).sal)
    highest_package=max(package)
    # avg_package=
    content = {'int_user':int_user, 'job_user':job_user,"total_student":total_student,
    "total_placed":total_placed,"highest_package":highest_package}
    return render(request, 'placement/index.html', content)

@allowed_users(allowed_roles=['Placement_Cell'])
def add_intership(request):
    form=IntershipForm()
    id=AdminDma.objects.get(name=request.user.username).id
    content={"form":form,"id":id}
    return render(request,"placement/add_intership.html",content)

@allowed_users(allowed_roles=['Placement_Cell'])
def form_intership(request):
    if request.method=="POST":
        form=IntershipForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Internship Added Successfully.")
            return redirect("placementIndex")
    return redirect("add_intership")

@allowed_users(allowed_roles=['Placement_Cell'])
def add_job(request):
    form=JobForm()
    id=AdminDma.objects.get(name=request.user.username).id
    if request.method=="POST":
        form=JobForm(request.POST)
        if form.is_valid():
            form.save()
            job = Job.objects.filter(adm_id=id).order_by("-id")[0]
            text = ""
            if job.cgpa != 0:
                text = text + f"<li class='text-left'>Minimum {job.cgpa} cgpa required</li>"
            if job.live_kt != "0":
                text = text + f"<li class='text-left'>Minimum {job.live_kt} KT </li>"
            if job.drop != "0":
                text = text + f"<li class='text-left'>Minimum {job.drop} year drop</li>"
            if text == "":
                text = "No Criteria"
            Job.objects.filter(id=job.id).update(who_can_apply=text)
            messages.success(request,"Job Added Successfully.")
            return redirect("placementIndex")
        else:
            messages.error(request,"Form is not valid")
    content={"form":form,"id":id}
    return render(request,"placement/add_job.html",content)

@allowed_users(allowed_roles=['Placement_Cell'])
def recruiting(request):
    jobs=Job.objects.filter(status=0)
    curr=Job.objects.filter(status=0,apply_by__gt=date.today())
    placed=Job_user.objects.filter(status=3)
    hired={}
    for job in jobs:
        count=0
        for p in placed:
            # print(p.job_id,job)
            if p.job_id==job:
                count+=1
        hired[job]=count
    context={"jobs":jobs,"curr":curr,"hired":hired}
    return render(request,"placement/recruiting.html",context)

@allowed_users(allowed_roles=['Placement_Cell'])
def recruited(request):
    jobs=Job.objects.filter(status=1)
    placed=Job_user.objects.filter(status=3)
    hired={}
    for job in jobs:
        count=0
        for p in placed:
            # print(p.job_id,job)
            if p.job_id==job:
                count+=1
        hired[job]=count
    context={"jobs":jobs,"hired":hired}
    return render(request,"placement/recruited.html",context)

@allowed_users(allowed_roles=['Placement_Cell'])
def details(request,id,type):
    if type==1:
        jobs = Job.objects.get(id=id)
        applied=Job_user.objects.filter(job_id=id)
        # print(applied)
        context={"details":jobs,"pay":"Salary","applied":applied,"id":id,"type":type}     
    elif type==2:
        internships = Intership.objects.get(id=id)
        context={"details":internships,"pay":"Stiped"}

    return render(request,"placement/details.html",context)

@allowed_users(allowed_roles=['Placement_Cell'])
def displayProfile(request,rollNo):
    student=Student.objects.get(roll_no=rollNo)
    user=User.objects.get(username=rollNo)
    name = user.first_name.upper()+' '+student.father_name.upper()+' '+user.last_name.upper()
    yearOfJoining='20'+rollNo[0:2]
    if rollNo[2:5]=="101":
        branch="INFT"
    elif rollNo[2:5]=="102":
        branch="CMPN"
    elif rollNo[2:5]=="103":
        branch="ETRX"
    elif rollNo[2:5]=="104":
        branch="EXTC"
    elif rollNo[2:5]=="105":
        branch="BIOMED"
    else:
        branch="Invalid User"

    div=rollNo[5]
    studentId=rollNo[6:]
    edu=Add_edu.objects.filter(roll_no=rollNo).order_by("degree")
    exp=Add_exp.objects.filter(rollNo=rollNo)

    context={"rollNo":rollNo,"student":student,"user":user,"name":name,"yearOfJoining":yearOfJoining,
    "branch":branch,"div":div,"studentId":studentId,"exp_list":exp,"edu_list":edu}
    return render(request,"placement/displayProfile.html",context) 

@allowed_users(allowed_roles=['Placement_Cell'])
def status(request):
    data = json.loads(request.body)
    st=data["status"]
    id=data["id"]
    Job_user.objects.filter(id=id).update(status=st)
    
    return JsonResponse('Done', safe=False)

def send_email(request,id,comp):
    job=Job.objects.get(id=comp)
    job_user=Job_user.objects.get(id=id)
    student=Student.objects.get(roll_no=job_user.roll_no)

    if job_user.status=='3':    
        
        send_accepted_email(student,job,request)
        Job_user.objects.filter(id=job_user.id).update(is_mail_send=True)
    elif job_user.status=='2':
        send_not_suitable_email(student,job,request)
    return redirect('/placement_cell/details/'+str(job.id)+"/1")