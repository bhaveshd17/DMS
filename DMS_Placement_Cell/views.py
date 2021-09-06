from django.http import JsonResponse
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


    try:
        highest_package = max(package)
        average_package = round(highest_package / len(package), 2)
    except:
        highest_package = 0
        average_package = 0
    if total_student or total_placed:
        total_placed = total_placed.count()
        total_student = total_student.count()
    else:
        total_placed = 0
        total_student = 0

    content = {'int_user':int_user, 'job_user':job_user,"total_student":total_student,
    "total_placed":total_placed,"highest_package":highest_package, 'average_package':average_package}
    return render(request, 'placement/index.html', content)


@allowed_users(allowed_roles=['Placement_Cell'])
def add_intership(request):
    form=IntershipForm()
    content={"form":form}
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
    if request.method=="POST":
        form=JobForm(request.POST)
        if form.is_valid():
            form.save()
            id = Job.objects.filter(comp_name=form.cleaned_data.get("comp_name")).order_by('-id')[0].id
            Job.objects.filter(id=id).update(who_can_apply=who_can_apply_text(id))
            messages.success(request,"Job Added Successfully.")
            return redirect("placementIndex")
        else:
            messages.error(request,"Form is not valid")
    content={"form":form}
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
    context = None
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

@allowed_users(allowed_roles=['Placement_Cell'])
def Update_Details(request,id):
    instance=Job.objects.get(id=id)
    form=JobForm(instance=instance)
    if request.method=="POST":
        form=JobForm(request.POST,instance=instance)
        print(form)
        if form.is_valid():
            form.save()
            Job.objects.filter(id=id).update(who_can_apply=who_can_apply_text(id))
            messages.success(request, 'Successfully Updated!')
            return redirect('/placement_cell/details/'+str(id)+"/1")
    content={"form":form,"id":id}
    return render(request,"placement/update_details.html",content)

@allowed_users(allowed_roles=['Placement_Cell'])
def delete_details(request,id):
    job =Job.objects.get(id=id)
    job.delete()
    messages.success(request, "Successfully deleted!")
    return redirect('recruiting')


def student_details(request):
    students = Student.objects.all()
    student_dict = {}
    for student in students:
        edu = Add_edu.objects.filter(roll_no=student)
        curr_edu = CurrEdu.objects.filter(roll_no_curr=student)
        certificate = Certificates.objects.filter(certificate_issued_to=student)
        experience = Add_exp.objects.filter(rollNo=student)
        user = User.objects.filter(username=student.roll_no)

        student_dict[student.roll_no] = [user, student, edu, curr_edu, certificate, experience]
    student_dict = sorted(student_dict.items())
    content = {'student_dict':student_dict}
    return render(request, 'placement/student_details.html', content)