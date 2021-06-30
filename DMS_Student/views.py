import operator

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import *
from .decorators import unauthenticated_user
from .form import SkillsForm
from .utils import IntershipJobLogic
from .filter_logic import intern_filters, job_filters

import json


@login_required(login_url='login')
def index(request):
    data = IntershipJobLogic(request)
    content = {'related_job_list': data['related_job_list'][:3], 'related_int_list': data['related_int_list'][:3]}
    return render(request, 'student/index.html', content)


@login_required(login_url='login')
def internship(request):
    data = IntershipJobLogic(request)

    content = {'related_int_list': data['related_int_list'],
               'skill_set':data['skill_set'],
               'duration':[1, 2, 3, 4, 6, 12, 24, 36],
               }
    return render(request, 'student/internship.html', content)

@login_required(login_url='login')
def internshipFilter(request):
    intern_data = intern_filters(request)
    internship_list = intern_data['internship']
    skill_set = intern_data['data']['skill_set']
    template = render_to_string('student/ajax_temp/internship.html',
                                {'related_int_list': internship_list,
                                 'skill_set':skill_set,
                                 'duration':[1, 2, 3, 4, 6, 12, 24, 36],
                                 })
    return JsonResponse({'data':template})


@login_required(login_url='login')
def job(request):
    data = IntershipJobLogic(request)
    content = {'related_job_list': data['related_job_list'],
               'skill_set':data['skill_set'],
               'cities':"Mumbai,Bangalore,Chennai".split(','),
               }
    return render(request, 'student/job.html', content)


@login_required(login_url='login')
def jobFilter(request):
    job_data = job_filters(request)
    job_list = job_data['job']
    skill_set = job_data['data']['skill_set']
    template = render_to_string('student/ajax_temp/jobs.html',
                                {'related_job_list': job_list,
                                 'skill_set':skill_set,
                                 'cities': "Mumbai,Bangalore,Chennai".split(','),
                                 })
    return JsonResponse({'data':template})



@login_required(login_url='login')
def preplacement(request):
    data = IntershipJobLogic(request)
    content = {'mock_test':data['mock_list']}
    return render(request, 'student/preplacement.html', content)

@login_required(login_url='login')
def details(request,id,type):
    content = {}
    if type==1:
        job_obj = Job.objects.get(id=id)
        try:
            job_user_obj = Job_user.objects.get(job_id=id, roll_no=request.user.username)
            status = job_user_obj.status

        except:
            status = '0'
        content={'details':job_obj, 'status':status, 'type':type, 'pay':'Salary'}
        
    elif type==2:
        internship_obj = Intership.objects.get(id=id)
        try:
            internship_user = Int_user.objects.get(roll_no=request.user.username, int_id=id)
            status = internship_user.status
        except:
            status = '0'

        content={'details':internship_obj, 'status':status, 'type':type, 'pay': 'Stipend'}

    return render(request,"student/details.html",content)


@login_required(login_url='login')
def apply(request):
    data = json.loads(request.body)
    type = data['user_details']['type']
    id = data['user_details']['id']
    status = data['user_details']['status']
    student = Student.objects.get(roll_no=request.user.username)
    if request.user.is_authenticated:
        if type == '1':
            job = Job.objects.get(id=id)
            job_user = Job_user(roll_no=student, job_id=job, status=status)
            job_user.save()

        elif type == '2':
            internship = Intership.objects.get(id=id)
            int_user = Int_user(roll_no=student, int_id=internship, status=status)
            int_user.save()

    return JsonResponse('Done', safe=False)


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
    elif rollNo[2:5]=="104":
        branch="EXTC"
    elif rollNo[2:5]=="105":
        branch="BIOMED"
    else:
        branch="Invalid User"

    div=rollNo[5]
    studentId=rollNo[6:]
    name=Student.objects.get(roll_no=request.user.username).name
    skills=Student.objects.get(roll_no=request.user.username).skills

    edu_list=[]
    exp_list=[]
    edu=Add_edu.objects.filter(roll_no=rollNo)
    exp=Add_exp.objects.filter(roll_no=rollNo)

    for e in edu:
        edu_list.append(e)
    for e in exp:
        exp_list.append(e)
    content={'rollNo':rollNo,'yearOfJoining':yearOfJoining,'branch':branch,'div':div,
    'studentId':studentId,"name":name,"skills":skills,'form':form,'edu_list':edu_list,'exp_list':exp_list}

    return render(request,"student/profile.html",content)

@login_required(login_url='login')
def updateEdu(request):
    student=Student.objects.get(roll_no=request.user.username)
    if request.method=="POST":
        clgname=request.POST['clgname']
        degree=request.POST['degree']
        marks=request.POST['marks']
        startyear=request.POST['startyear']
        endyear=request.POST['endyear']
        add,created=Add_edu.objects.get_or_create(clg_name=clgname,degree=degree,marks=marks,start_year=startyear,end_year=endyear,roll_no=student)
        add.save()
        messages.success(request, 'Successfully Added')
        return redirect('/student/profile')
    else:
        messages.error(request, 'Invalid Addition')
        return redirect('/student/profile')

@login_required(login_url='login')
def updateExp(request):
    student=Student.objects.get(roll_no=request.user.username)
    if request.method=="POST":
        compname=request.POST['compname']
        domain=request.POST['role']
        joindate=request.POST['joindate']
        duration=request.POST['duration']
        add,created=Add_exp.objects.get_or_create(comp_name=compname,role=domain,duration=duration,roll_no=student,start_date=joindate)
        add.save()
        messages.success(request, 'Successfully Added')
        return redirect('/student/profile')
    else:
        messages.error(request, 'Invalid Addition')
        return redirect('/student/profile')


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


@login_required(login_url='login')
def search(request):
    search_list = {}
    search=request.GET['to_search']
    query=search.lower()
    jobs = Job.objects.filter(Q(skills__icontains=query) | Q(comp_name__icontains=query))
    internships = Intership.objects.filter(Q(skills__icontains=query) | Q(comp_name__icontains=query))
    for job in jobs:
        search_list[job] = 1
    for internship in internships:
        search_list[internship] = 2

    search_list = dict(sorted(search_list.items(), key=operator.itemgetter(1), reverse=True))

            
    content = {"search_list":search_list, "query":query}
    return render(request,"student/search.html",content)

@login_required(login_url='login')
def userApplication(request):
    job_user = Job_user.objects.filter(roll_no=request.user.username)
    int_user = Int_user.objects.filter(roll_no=request.user.username)
    applied_dict = {}
    for job_u in job_user:
        job = Job.objects.get(id=job_u.job_id.id)
        applied_dict[job] = 1
    for intern_u in int_user:
        internship = Intership.objects.get(id=intern_u.int_id.id)
        applied_dict[internship] = 2

    content = {"applied_dict":applied_dict}
    return render(request,'student/userApplication.html',content)





# authentication
@unauthenticated_user
def handleLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session.set_expiry(60*60*24)
            if user.is_staff:
                return redirect("placementIndex")
            return redirect('/student/')
        else:
            messages.error(request, 'Wrong username or password')
            return render(request, 'authentication/login.html')

    return render(request, 'authentication/login.html')

def handelLogout(request):
    logout(request)
    return redirect('/login/')
