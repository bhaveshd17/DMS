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
    total_student=Student.objects.all()
    total_placed=Job_user.objects.filter(status="3").distinct()
    package=[]
    highest=Job_user.objects.filter(status="3")
    for job in highest:
        package.append(Job.objects.get(id=job.job_id.id).sal)

    if total_student or total_placed or package:
        total_placed = total_placed.count()
        total_student = total_student.count()
        highest_package = max(package)
    else:
        total_placed = 0
        total_student = 0
        highest_package = 0
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
            if job.aggregate_sgpi != "NA":
                text = text + f"<li class='text-left'>Minimum {job.aggregate_sgpi} SGPI required</li>"
            if job.ssc_percentage != "NA":
                text = text + f"<li class='text-left'>Minimum {job.ssc_percentage} % of 10th required </li>"
            if job.hsc_d_percentage != "NA":
                text = text + f"<li class='text-left'>Minimum {job.hsc_d_percentage} % of 12/diploma required</li>"
            if job.live_kt != "NA":
                text = text + f"<li class='text-left'>Minimum {job.live_kt} Live KT </li>"
            if job.dead_kt != "NA":
                text = text + f"<li class='text-left'>Minimum {job.dead_kt} Dead KT</li>"
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
    student = Student.objects.get(roll_no=rollNo)
    user = User.objects.get(username=student.roll_no)
    name = user.first_name
    yearOfJoining = '20' + rollNo[0:2]
    branch = student.branch
    div = student.div
    studentId = rollNo[6:]
    exp = Add_exp.objects.filter(rollNo=rollNo)
    edu = Add_edu.objects.filter(roll_no=rollNo).order_by("degree")
    prev_deg = [edu.degree for edu in edu]

    curr_edu = CurrEdu.objects.filter(roll_no_curr=rollNo)
    certificate_list = Certificates.objects.filter(certificate_issued_to=rollNo)

    content = {'rollNo': rollNo, 'yearOfJoining': yearOfJoining, 'branch': branch, 'div': div,
               'studentId': studentId, 'edu_list': edu, 'exp_list': exp,
               'student_info': student, 'name': name,'user':user,
               'prev_deg': prev_deg, 'certificate_list': certificate_list, 'curr_edu': curr_edu}
    return render(request, "placement/displayProfile.html", content)

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