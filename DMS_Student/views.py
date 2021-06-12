from django.shortcuts import render

def index(request):
    content = {}
    return render(request, 'student/index.html', content)

def internship(request):
    content = {}
    return render(request, 'student/internship.html', content)

def preplacement(request):
    content = {}
    return render(request, 'student/preplacement.html', content)
