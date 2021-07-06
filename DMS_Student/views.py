import operator

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import *
from .decorators import unauthenticated_user
from .form import SkillsForm, AddEduForm, AddExpForm, FeForm, SeForm, TeForm, BeForm
from .utils import branch_logic, be_year_logic, department_sort, jobLogic, internshipLogic
from .filter_logic import intern_filters, job_filters

import json

@login_required(login_url='login')
def index(request):
    internship = internshipLogic(request)
    job = jobLogic(request)
    content = {'related_job_list': job['related_job_list'][:3], 'related_int_list': internship['related_int_list'][:3]}
    return render(request, 'student/index.html', content)


@login_required(login_url='login')
def internship(request):
    data = internshipLogic(request)

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
    data = jobLogic(request)
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
    data = department_sort(request)
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
    name = request.user.first_name.upper()+' '+student.father_name.upper()+' '+request.user.last_name.upper()
    yearOfJoining='20'+rollNo[0:2]
    branch = branch_logic(rollNo)
    prev_edu = Add_edu.objects.filter(roll_no=request.user.username)
    prev_deg = [edu.degree for edu in prev_edu]
    div=rollNo[5]
    studentId=rollNo[6:]
    edu=Add_edu.objects.filter(roll_no=rollNo).order_by("degree")
    exp=Add_exp.objects.filter(rollNo=rollNo)

    skill_form=SkillsForm(instance=student)
    edu_form = AddEduForm()
    exp_form = AddExpForm()
    fe_form = FeForm()
    se_form = SeForm()
    te_form = TeForm()
    be_form = BeForm()
    fe = FE.objects.filter(roll_no_1=rollNo)
    se = SE.objects.filter(roll_no_2=rollNo)
    te = TE.objects.filter(roll_no_3=rollNo)
    be = BE.objects.filter(roll_no_4=rollNo)



    content={'rollNo':rollNo,'yearOfJoining':yearOfJoining,'branch':branch,'div':div,
             'studentId':studentId,'skill_form':skill_form,'edu_list':edu,'exp_list':exp,
             'student_info':student, 'name':name, 'edu_form':edu_form, 'exp_form':exp_form,
             'fe_form':fe_form, 'se_form':se_form, 'te_form':te_form, 'be_form':be_form,
             'fe':fe,'se':se,'te':te,'be':be, 'prev_deg':prev_deg}
    return render(request,"student/profile.html",content)


@login_required(login_url='login')
def add_education(request):
    if request.method=="POST":
        form = AddEduForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Added')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid Addition')
            return redirect('profile')

@login_required(login_url='login')
def update_education(request, pk):
    csrf_token_value = request.COOKIES['csrftoken']
    instance = get_object_or_404(Add_edu, id=pk)
    form = AddEduForm(instance=instance)
    if request.method == "POST":
        form = AddEduForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid Entry')
            return redirect('profile')

    template = render_to_string('student/ajax_temp/add_edu.html',
                                {'id':pk, 'csrf_token_value':csrf_token_value,'edu':instance, 'form':form})
    return JsonResponse({'data':template})

@login_required(login_url='login')
def delete_education(request, pk):
    add_edu = Add_edu.objects.get(id=pk)
    add_edu.delete()
    messages.success(request, f"{add_edu} successfully deleted!")
    return redirect('profile')



@login_required(login_url='login')
def add_experience(request):
    if request.method=="POST":
        form = AddExpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Added')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid Addition')
            return redirect('profile')

@login_required(login_url='login')
def update_experience(request, pk):
    csrf_token_value = request.COOKIES['csrftoken']
    instance = get_object_or_404(Add_exp, id=pk)
    form = AddExpForm(instance=instance)
    if request.method == "POST":
        form = AddExpForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid Entry')
            return redirect('profile')

    template = render_to_string('student/ajax_temp/add_exp.html',
                                {'id':pk, 'csrf_token_value':csrf_token_value, 'form':form})
    return JsonResponse({'data':template})

@login_required(login_url='login')
def delete_experience(request, pk):
    add_exp = Add_exp.objects.get(id=pk)
    add_exp.delete()
    messages.success(request, f"{add_exp} successfully deleted!")
    return redirect('profile')


@login_required(login_url='login')
def add_curr_education(request):
    year = request.GET.get('year')
    if request.method == 'POST':
        data = be_year_logic(request=request, year=year)
        form = data['form']
        if form.is_valid():
            form.save()
            messages.success(request, f"successfully added!")
            return redirect('profile')
        else:
            messages.error(request, f"invalid entry!")
            return redirect('profile')

@login_required(login_url='login')
def update_curr_education(request, pk, year):
    csrf_token_value = request.COOKIES['csrftoken']
    if request.method == "POST":
        form_data = be_year_logic(request=request, year=year, pk=pk)
        form = form_data['form']
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid Entry')
            return redirect('profile')

    template_data = be_year_logic(request=request, year=year, csrf_token_value=csrf_token_value, pk=pk, template_stat=1)
    template = template_data['template']
    return JsonResponse({'data':template})

@login_required(login_url='login')
def delete_curr_education(request, pk):
    year = request.GET.get('year')
    data = be_year_logic(request=request, year=year, pk=pk)
    obj = data['del_obj']
    obj.delete()
    messages.success(request, "successfully deleted!")
    return redirect('profile')


@login_required(login_url='login')
def add_certificates(request):
    return redirect('profile')




@login_required(login_url='login')
def UpdateSkills(request):
    csrf_token_value = request.COOKIES['csrftoken']
    rollNo = request.user.username
    student = Student.objects.get(roll_no=rollNo)
    form = SkillsForm(instance=student)
    if request.method == "POST":
        form = SkillsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid Update')
            return redirect('profile')

    template = render_to_string('student/ajax_temp/update_skills.html',
                                {'form': form, 'csrf_token_value':csrf_token_value })
    return JsonResponse({'data': template})




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



