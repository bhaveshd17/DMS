from django.shortcuts import render
from DMS_Student.models import *

def index(request):
    int_user = Int_user.objects.all().order_by("id")
    job_user = Job_user.objects.all().order_by("id")
    content = {'int_user':int_user, 'job_user':job_user}
    return render(request, 'placement/index.html', content)
