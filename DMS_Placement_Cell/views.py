from django.shortcuts import render
from .form import *

def index(request):
    content = {}
    return render(request, 'index.html', content)

def add_intership(request):
    form=IntershipForm()
    content={"form":form}
    return render(request,"add_intership.html",content)