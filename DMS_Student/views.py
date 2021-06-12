from django.shortcuts import render

def home(request):
    content = {}
    return render(request, 'student/home.html', content)
