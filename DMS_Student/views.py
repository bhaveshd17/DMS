from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user

@login_required(login_url='login')
def index(request):
    job_obj = Job.objects.all()
    job_list = []
    for job in job_obj:
        job_list.append(job)

    int_obj = Intership.objects.all()
    int_list = []
    for intern in int_obj:
        int_list.append(intern)
    
    content = {'job_list':job_list[:3], 'int_list': int_list[:3]}
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
