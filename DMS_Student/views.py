from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .decorators import unauthenticated_user
from .form import SkillsForm
from .utils import IntershipJobLogic

@login_required(login_url='login')
def index(request):
    data = IntershipJobLogic(request)
    content = {'related_job_list': data['related_job_list'][:3], 'related_int_list': data['related_int_list'][:3]}
    return render(request, 'student/index.html', content)


@login_required(login_url='login')
def internship(request):
    data = IntershipJobLogic(request)
    content = {'related_int_list': data['related_int_list']}
    return render(request, 'student/internship.html', content)


@login_required(login_url='login')
def preplacement(request):
    data = IntershipJobLogic(request)
    content = {'mock_test':data['mock_list']}
    return render(request, 'student/preplacement.html', content)


@login_required(login_url='login')
def job(request):
    data = IntershipJobLogic(request)
    content = {'related_job_list': data['related_job_list']}
    return render(request, 'student/job.html', content)

@login_required(login_url='login')
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

@login_required(login_url='login')
def UpdateSkills(request):
    rollNo=request.user.username
    student=Student.objects.get(roll_no=rollNo)
    if request.method=="POST":
        form=SkillsForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated')
            return redirect('/student/profile')
        else:
            messages.error(request, 'Invalid Update')
            return redirect('/student/profile')


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
