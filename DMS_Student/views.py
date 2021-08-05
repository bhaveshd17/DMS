from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages.api import error
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse

from .decorators import unauthenticated_user
from .form import SkillsForm, AddEduForm, AddExpForm, CurrEduForm, StudentForm, CertificateForm, UserForm
from .utils import *
from .filter_logic import intern_filters, job_filters

import json
import operator
import re

from .validation import isValidPassportNo, isValidPanCardNo


@login_required(login_url='login')
def index(request):
    internship = internshipLogic(request)
    job = jobLogic(request)
    content = {'related_job_list': job['department_wise_job'][:3],
               'related_int_list': internship['related_int_list'][:3]}
    return render(request, 'student/index.html', content)


@login_required(login_url='login')
def internship(request):
    data = internshipLogic(request)

    content = {'related_int_list': data['related_int_list'],
               'skill_set': data['skill_set'],
               'duration': [1, 2, 3, 4, 6, 12, 24, 36],
               }
    return render(request, 'student/internship.html', content)


@login_required(login_url='login')
def internshipFilter(request):
    intern_data = intern_filters(request)
    internship_list = intern_data['internship']
    skill_set = intern_data['data']['skill_set']
    template = render_to_string('student/ajax_temp/internship.html',
                                {'related_int_list': internship_list,
                                 'skill_set': skill_set,
                                 'duration': [1, 2, 3, 4, 6, 12, 24, 36],
                                 })
    return JsonResponse({'data': template})


@login_required(login_url='login')
def job(request):
    data = jobLogic(request)
    content = {'related_job_list': data['related_job_list'],
               'skill_set': data['skill_set'],
               'cities': data['cities'],
               }
    return render(request, 'student/job.html', content)


@login_required(login_url='login')
def jobFilter(request):
    job_data = job_filters(request)
    job_list = job_data['job']
    skill_set = job_data['data']['skill_set']

    template = render_to_string('student/ajax_temp/jobs.html',
                                {'related_job_list': job_list,
                                 'skill_set': skill_set,
                                 'cities': job_data['data']['cities'],
                                 })
    return JsonResponse({'data': template})


@login_required(login_url='login')
def all_job(request):
    data = jobLogic(request)
    content = {'related_job_list': data['department_wise_job'],
               'skill_set': data['skill_set'],
               'cities': data['cities'],
               }
    return render(request, 'student/all_jobs.html', content)


@login_required(login_url='login')
def preplacement(request):
    data = department_sort(request)
    content = {'mock_test': data['mock_list']}
    return render(request, 'student/preplacement.html', content)


@login_required(login_url='login')
def details(request, id, type):
    content = {}
    if type == 1:
        data = jobLogic(request)
        related_job_list = data['related_job_list']
        job_obj = Job.objects.get(id=id)

        try:
            job_user_obj = Job_user.objects.get(job_id=id, roll_no=request.user.username)
            status = job_user_obj.status

        except:
            status = '0'
        content = {'details': job_obj,
                   'status': status,
                   'type': type,
                   'pay': 'Salary',
                   'related_job_list': related_job_list,
                   'related_int_list':[]}

    elif type == 2:
        data = internshipLogic(request)
        related_int_list = data['related_int_list']
        internship_obj = Intership.objects.get(id=id)
        try:
            internship_user = Int_user.objects.get(roll_no=request.user.username, int_id=id)
            status = internship_user.status
        except:
            status = '0'

        content = {'details': internship_obj,
                   'status': status,
                   'type': type,
                   'pay': 'Stipend',
                   'related_int_list': related_int_list,
                   'related_job_list': []}

    return render(request, "student/details.html", content)


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
    rollNo = request.user.username
    student = Student.objects.get(roll_no=rollNo)
    name = request.user.first_name.upper()
    yearOfJoining = '20' + rollNo[0:2]
    branch = student.branch
    div = student.div
    studentId = rollNo[6:]
    exp = Add_exp.objects.filter(rollNo=rollNo)
    edu = Add_edu.objects.filter(roll_no=rollNo).order_by("degree")
    prev_deg = [edu.degree for edu in edu]

    skill_form = SkillsForm(instance=student)
    edu_form = AddEduForm()
    exp_form = AddExpForm()
    curr_education_form = CurrEduForm()
    certificate_form = CertificateForm()
    curr_edu = CurrEdu.objects.filter(roll_no_curr=rollNo)
    certificate_list = Certificates.objects.filter(certificate_issued_to=rollNo)

    content = {'rollNo': rollNo, 'yearOfJoining': yearOfJoining, 'branch': branch, 'div': div,
               'studentId': studentId, 'skill_form': skill_form, 'edu_list': edu, 'exp_list': exp,
               'student_info': student, 'name': name, 'edu_form': edu_form, 'exp_form': exp_form,
               'curr_education_form': curr_education_form, 'certificate_form': certificate_form,
               'prev_deg': prev_deg, 'certificate_list': certificate_list, 'curr_edu': curr_edu}
    return render(request, "student/profile.html", content)


@login_required(login_url='login')
def add_education(request):
    if request.method == "POST":
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
                                {'id': pk, 'csrf_token_value': csrf_token_value, 'edu': instance, 'form': form})
    return JsonResponse({'data': template})


@login_required(login_url='login')
def delete_education(request, pk):
    add_edu = Add_edu.objects.get(id=pk)
    add_edu.delete()
    messages.success(request, f"{add_edu} successfully deleted!")
    return redirect('profile')


@login_required(login_url='login')
def add_experience(request):
    if request.method == "POST":
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
                                {'id': pk, 'csrf_token_value': csrf_token_value, 'form': form})
    return JsonResponse({'data': template})


@login_required(login_url='login')
def delete_experience(request, pk):
    add_exp = Add_exp.objects.get(id=pk)
    add_exp.delete()
    messages.success(request, f"{add_exp} successfully deleted!")
    return redirect('profile')


@login_required(login_url='login')
def add_curr_education(request):
    if request.method == 'POST':
        form = CurrEduForm(request.POST)
        if form.is_valid():
            form.save()
            edu = [deg.degree for deg in Add_edu.objects.filter(roll_no=request.user.username)]
            if "diploma" in edu:
                sgpi3 = float(form.cleaned_data.get('sgpi3'))
                sgpi4 = float(form.cleaned_data.get('sgpi4'))
                CurrEdu.objects.filter(roll_no_curr=request.user.username).update(total_grade=sgpi3 + sgpi4)
                CurrEdu.objects.filter(roll_no_curr=request.user.username).update(
                    average_sgpi=round((sgpi3 + sgpi4) / 2, 2))
            else:
                sgpi1 = float(form.cleaned_data.get('sgpi1'))
                sgpi2 = float(form.cleaned_data.get('sgpi2'))
                CurrEdu.objects.filter(roll_no_curr=request.user.username).update(total_grade=sgpi1 + sgpi2)
                CurrEdu.objects.filter(roll_no_curr=request.user.username).update(
                    average_sgpi=round((sgpi1 + sgpi2) / 2, 2))
            messages.success(request, 'Successfully Added')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid Addition')
            return redirect('profile')


@login_required(login_url='login')
def update_curr_education(request, pk):
    csrf_token_value = request.COOKIES['csrftoken']
    instance = get_object_or_404(CurrEdu, id=pk)
    form = CurrEduForm(instance=instance)
    prev_degree = [deg.degree for deg in Add_edu.objects.filter(roll_no=request.user.username)]
    if request.method == "POST":
        form = CurrEduForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            sgpi_list = []
            for key, value in data.items():
                if re.search('^sgpi', key) and value != "NA":
                    sgpi_list.append(float(value))

            CurrEdu.objects.filter(id=pk).update(total_grade=sum(sgpi_list))
            CurrEdu.objects.filter(id=pk).update(average_sgpi=round(sum(sgpi_list) / len(sgpi_list), 2))

            messages.success(request, 'Successfully Updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid Entry')
            return redirect('profile')

    template = render_to_string('student/ajax_temp/add_curr_edu.html',
                                {'id': pk, 'csrf_token_value': csrf_token_value, 'form': form,
                                 'prev_degree': prev_degree, 'curr_edu': instance})
    return JsonResponse({'data': template})


@login_required(login_url='login')
def delete_curr_education(request, pk):
    curr_edu = CurrEdu.objects.get(id=pk)
    curr_edu.delete()
    messages.success(request, f"successfully deleted!")
    return redirect('profile')


@login_required(login_url='login')
def add_certificates(request):
    if request.method == "POST":
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Added')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid Addition')
            return redirect('profile')


@login_required(login_url='login')
def update_certificate(request, pk):
    csrf_token_value = request.COOKIES['csrftoken']
    instance = get_object_or_404(Certificates, id=pk)
    form = CertificateForm(instance=instance)
    if request.method == "POST":
        form = CertificateForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid Entry')
            return redirect('profile')

    template = render_to_string('student/ajax_temp/update_certificate.html',
                                {'id': pk, 'csrf_token_value': csrf_token_value, 'form': form})
    return JsonResponse({'data': template})


@login_required(login_url='login')
def delete_certificates(request, pk):
    certificate = Certificates.objects.get(id=pk)
    certificate.delete()
    messages.success(request, f"successfully deleted!")
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
                                {'form': form, 'csrf_token_value': csrf_token_value})
    return JsonResponse({'data': template})

@login_required(login_url='login')
def update_personal(request, pk):
    student = Student.objects.get(roll_no=pk)
    user = User.objects.get(username=pk)
    student_form = StudentForm(instance=student)
    content = {'student_form':student_form, 'student':student, 'user':user}
    if request.method == 'POST':
        student_form = StudentForm(request.POST, request.FILES, instance=student)
        if student_form.is_valid():
            student_form.save()
            messages.success(request, 'Successfully Updated')
            return redirect('profile')
        else:
            messages.success(request, 'Failed')
            return redirect('profile')

    return render(request, 'student/update_personal.html', content)


@login_required(login_url='login')
def search(request):
    search_list = {}
    search = request.GET['to_search']
    query = search.lower()
    jobs = Job.objects.filter(Q(skills__icontains=query) | Q(comp_name__icontains=query))
    internships = Intership.objects.filter(Q(skills__icontains=query) | Q(comp_name__icontains=query))
    for job in jobs:
        search_list[job] = 1
    for internship in internships:
        search_list[internship] = 2

    search_list = dict(sorted(search_list.items(), key=operator.itemgetter(1), reverse=True))

    content = {"search_list": search_list, "query": query}
    return render(request, "student/search.html", content)


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

    content = {"applied_dict": applied_dict}
    return render(request, 'student/userApplication.html', content)


# authentication
@unauthenticated_user
def handleLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        student=Student.objects.filter(roll_no=username)
        if student:
            flag = student[0].is_email_verified
        else:
            flag = True

        if flag:
            if user is not None:
                login(request, user)
                request.session.set_expiry(60*60*24)
                if user.is_staff:
                    return redirect("placementIndex")
                return redirect('/student/')
            else:
                messages.error(request, 'Wrong username or password')
                return render(request, 'authentication/login.html')
        else:
            messages.error(request, 'Please Verify the Email')

    return render(request, 'authentication/login.html')


def handelLogout(request):
    logout(request)
    return redirect('login')


def register(request):
    student_form=StudentForm()
    user_form=UserForm()
    if request.method=="POST":
        student_form=StudentForm(request.POST,request.FILES)
        user_form=UserForm(request.POST)
        if student_form.is_valid() and user_form.is_valid():
            pan_no = student_form.cleaned_data.get("pan_card_no")
            passport_number = student_form.cleaned_data.get("passport_no")
            if isValidPassportNo(passport_number):
                if isValidPanCardNo(pan_no):
                    student_form.save()
                    user_form.save()
                    username = user_form.cleaned_data.get("username")
                    student = Student.objects.get(roll_no=username)
                    name = user_form.cleaned_data.get("first_name")
                    send_action_email(student, name, request)
                    messages.success(request, f"your username is sent on email")
                    return redirect("login")
                else:
                    messages.error(request, f"Invalid pan card number")
                    return redirect("register")
            else:
                messages.warning(request, f"Invalid passport number")
                return redirect("register")
        else:
            messages, error(request, "Failed")
    content = {"student_form": student_form, "user_form": user_form}
    return render(request, "authentication/register.html", content)


def activate_user(request, uidb64, token):
    try:
        uid=force_text(urlsafe_base64_decode(uidb64))
        student=Student.objects.get(roll_no=uid)
    except Exception as e:
        student=None
    
    if student and generate_token.check_token(student,token):
        student.is_email_verified=True
        student.save()

        messages.success(request,"Email is Verified")
        return redirect(reverse('login'))
    content={"student":student}
    return render(request,'authentication/activate_fail.html',content)

 
