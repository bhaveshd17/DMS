from django.shortcuts import render

def index(request):
    content = {}
    return render(request, 'student/index.html', content)
