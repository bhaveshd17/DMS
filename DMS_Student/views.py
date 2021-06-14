from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user

from .form import SkillsForm

@login_required(login_url='login')
def index(request):
    roll_no = request.user.username
    student_obj = Student.objects.get(roll_no=roll_no)
    skills = student_obj.skills
    sk_list = skills.split(',')
    sk_set = set()
    for skill in sk_list:
        job = Job.objects.filter(skills__icontains=skill)
        if not job.count():
            continue
        sk_set.add(job[0].skills)
    print(sk_set)

    job_obj = Job.objects.filter(skills__icontains=skills)
    print(job_obj)
    job_list = []
    for job in job_obj:
        job_list.append(job)

    int_obj = Intership.objects.all()
    int_list = []
    for intern in int_obj:
        int_list.append(intern)
    
    content = {'job_list':job_list, 'int_list': int_list[:3]}
    return render(request, 'student/index.html', content)


@login_required(login_url='login')
def internship(request):
    int_obj = Intership.objects.all()
    content = {'int_obj':int_obj}
    return render(request, 'student/internship.html', content)


@login_required(login_url='login')
def preplacement(request):
    mock_test= Mock_test.objects.all()
    content = {'mock_test':mock_test}
    return render(request, 'student/preplacement.html', content)


@login_required(login_url='login')
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

@login_required(login_url='login')
def profile(request):
    rollNo=request.user.username
    student=Student.objects.get(roll_no=rollNo)
    form=SkillsForm(instance=student)
    yearOfJoining='20'+rollNo[0:2]
    if rollNo[2:5]=="101":
        branch="INFT"
    elif rollNo[2:5]=="102":
        branch="CMPN"
    elif rollNo[2:5]=="103":
        branch="ETRX"
    else:
        branch="Invalid User"

    div=rollNo[5]
    studentId=rollNo[6:]
    name=Student.objects.get(roll_no=request.user.username).name
    skills=Student.objects.get(roll_no=request.user.username).skills
    content={'rollNo':rollNo,'yearOfJoining':yearOfJoining,'branch':branch,'div':div,'studentId':studentId,"name":name,"skills":skills,'form':form}

    return render(request,"student/profile.html",content)

def UpdateSkills(request):
    rollNo=request.user.username
    student=Student.objects.get(roll_no=rollNo)
    if request.method=="POST":
        form=SkillsForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/student/profile')
        else:
            messages.error(request, 'Invalid Update')


# authentication
@unauthenticated_user
def handleLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/student/')
        else:
            messages.error(request, 'Wrong username or password')
            return render(request, 'authentication/login.html')

    return render(request, 'authentication/login.html')

def handelLogout(request):
    logout(request)
    return redirect('/login/')
