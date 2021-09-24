from collections import OrderedDict

from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from .form import *
from DMS_Student.decorators import allowed_users
from DMS_Student.models import *
from datetime import date
from django.contrib.auth.models import User
import json
import math
import pandas as pd
from .utils import *


@allowed_users(allowed_roles=['Placement_Cell'])
def index(request):
    student_data = Student.objects.all()
    offer_data = Job_user.objects.filter(status="3")
    placed_data=Student.objects.filter(placed=True)
    package = []

    for job in offer_data:
        package.append(float(job.salary))
   
    try:
        highest_package = max(package)
        lowest_package=min(package)
        average_package = float(math.ceil(sum(package) / len(package)))
    except:
        highest_package = 0
        lowest_package=0
        average_package = 0
    if student_data or offer_data or offer_data:
        total_offer=len(offer_data)
        total_placed = len(placed_data)
        total_student = len(student_data)
    else:
        total_placed = 0
        total_student = 0

    labelDiv = ["INFT", "CMPN", "EXTC", "ETRX", "BIOM"]
    dataDiv = []
    dataMale = []
    dataFemale = []
    dataPMale=[]
    dataPFemale=[]
    for i in labelDiv:
        branch = Student.objects.filter(branch=i)
        dataDiv.append(len(branch))
        male = 0
        Pmale=0
        female = 0
        Pfemale=0
        for student in branch:
            if student.gender == "Male":
                male = male + 1
                if student.placed:Pmale+=1
            else:
                female = female + 1
                if student.placed:Pfemale+=1
        dataMale.append(male)
        dataFemale.append(female)
        dataPFemale.append(Pfemale)
        dataPMale.append(Pmale)

    labelCTC = ["0 to 3.49 LPA", "3.50 to 4.99 LPA", "5.00 to 7.00 LPA", "7.01 and Above"]
    ctc = []
    first = 0
    second = 0
    third = 0
    fourth = 0
    for i in offer_data:
        if int(i.salary) >= 0 and int(i.salary) <= 349000:
            first = first + 1
        elif int(i.salary) >= 350000 and int(i.salary) <= 499000:
            second = second + 1
        elif int(i.salary) >= 500000 and int(i.salary) <= 700000:
            third = third + 1
        elif int(i.salary) >= 701000:
            fourth = fourth + 1
    ctc.append(first)
    ctc.append(second)
    ctc.append(third)
    ctc.append(fourth)
    # Value missmatch in excel and graph

    labelSector = ["Automotive", "Banking", "EduTech", "Financial Services", "Information Technology","Logistics & Supply Chain", "Retail", "Telecommunications", "Electrical Manufacturing",
                   "Marketing & Advertising", "Media Production", "Management Consulting", "Manufacturing",
                   "Health Care", "Design", "Professional Services"]

    sectorCount = [None] * 16

    for s in offer_data:
        job = Job.objects.get(id=s.job_id.id)
        i = labelSector.index(job.domain)
        if sectorCount[i] == None:
            sectorCount[i] = 1
        else:
            sectorCount[i] = sectorCount[i] + 1



    content = {"total_student": total_student,
               "total_placed": total_placed,
               "highest_package": highest_package, "lowest_package":lowest_package,'average_package': average_package,"total_offer":total_offer, "labelDiv": labelDiv,
               "dataDiv": dataDiv, "dataMale": dataMale, "dataFemale": dataFemale, "dataPMale":dataPMale,"dataPFemale":dataPFemale,"ctc": ctc, "labelCTC": labelCTC,
               "labelSector": labelSector, "sectorCount": sectorCount}
    return render(request, 'placement/index.html', content)


@allowed_users(allowed_roles=['Placement_Cell'])
def ctcWise(request):
    offer_data = Job_user.objects.filter(status="3")
    labelCTC = ["0 to 3.49 LPA", "3.50 to 4.99 LPA", "5.00 to 7.00 LPA", "7.01 and Above"]
    ctc_dict = {}
    fl, sl, tl, frl = [],[],[],[]
    job_dataframe = pd.DataFrame([])
    for data in offer_data:
        job_dataframe = job_dataframe.append({'salary':data.salary, 'company':data.job_id.comp_name}, ignore_index=True)
    data = job_dataframe[["salary", "company"]].value_counts()
    data = data.to_frame()

    for i, row in data.iterrows():
        if int(i[0]) >= 0 and int(i[0]) <= 349000:
            fl.append({i[1]:[i[0], row[0]]})
            ctc_dict[labelCTC[0]] = fl
        elif int(i[0]) >= 350000 and int(i[0]) <= 499000:
            sl.append({i[1]: [i[0], row[0]]})
            ctc_dict[labelCTC[1]] = sl
        elif int(i[0]) >= 500000 and int(i[0]) <= 700000:
            tl.append({i[1]: [i[0], row[0]]})
            ctc_dict[labelCTC[2]] = tl
        elif int(i[0]) >= 701000:
            frl.append({i[1]: [i[0], row[0]]})
            ctc_dict[labelCTC[3]] = frl

    ctc =[]
    for key, value in ctc_dict.items():
        ls = []
        for data in value:
            for i, j in data.items():
                ls.append(j[1])
        ctc.append(sum(ls))
    # print(ctc_dict)
    content = {'labelCTC':labelCTC, 'ctc':ctc, 'ctc_dict':ctc_dict}
    return render(request, "placement/ctc.html", content)

@allowed_users(allowed_roles=['Placement_Cell'])
def gender_ratio(request):
    student_dataframe = pd.DataFrame([])
    for student in Student.objects.all():
        student_dataframe = student_dataframe.append({'roll_no':student.roll_no, 'gender':student.gender, 'placed':student.placed, 'branch': student.branch, 'div':student.div}, ignore_index=True)
    div_data = student_dataframe[['branch', 'div', 'placed', 'gender']].value_counts()
    div_data = div_data.to_frame()
    gender_dict = {}
    dataMale, dataFemale, dataPMale, dataPFemale = [], [], [], []
    labelDiv = set([data[0]+' '+data[1] for data, count in div_data.iterrows()])
    for label in labelDiv:
        gender_dict[label] = {}
        gender_dict[label]['ptotal'] = 0
        gender_dict[label]['grand_total'] = 0
        gender_dict[label]['male'] = 0
        gender_dict[label]['female'] = 0

    for data, count in div_data.iterrows():
        branch = data[0] + ' ' + data[1]
        gender_dict[branch]['grand_total'] += count[0]
        if data[3].lower() == 'male':
            gender_dict[branch]['male'] += count[0]
        elif data[3].lower() == 'female':
            gender_dict[branch]['female'] += count[0]

        if data[2] == 1:
            gender_dict[branch]['ptotal'] += count[0]
            if data[3].lower() == 'male':
                gender_dict[branch]['pmale'] = count[0]
            elif data[3].lower() == 'female':
                gender_dict[branch]['pfemale'] = count[0]

    total_student = []
    total_placed = []
    dic = OrderedDict(sorted(gender_dict.items()))
    for key, value in dic.items():
        dataFemale.append(value['female'])
        dataMale.append(value['male'])
        dataPFemale.append(value['pfemale'])
        dataPMale.append(value['pmale'])
        total_placed.append(value['ptotal'])
        total_student.append(value['grand_total'])


    content = {'labelDiv':sorted(labelDiv), 'dataMale':dataMale, 'dataFemale':dataFemale, 'dataPMale':dataPMale, 'dataPFemale':dataPFemale, 'dic':dic, 'total_student':sum(total_student),'total_placed':sum(total_placed) }
    return render(request, "placement/gender_ratio.html", content)

@allowed_users(allowed_roles=['Placement_Cell'])
def add_intership(request):
    form = IntershipForm()
    content = {"form": form}
    return render(request, "placement/add_intership.html", content)


@allowed_users(allowed_roles=['Placement_Cell'])
def form_intership(request):
    if request.method == "POST":
        form = IntershipForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Internship Added Successfully.")
            return redirect("placementIndex")
    return redirect("add_intership")


@allowed_users(allowed_roles=['Placement_Cell'])
def add_job(request):
    form = JobForm()
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            id = Job.objects.filter(comp_name=form.cleaned_data.get("comp_name")).order_by('-id')[0].id
            Job.objects.filter(id=id).update(who_can_apply=who_can_apply_text(id))
            messages.success(request, "Job Added Successfully.")
            return redirect("placementIndex")
        else:
            messages.error(request, "Form is not valid")
    content = {"form": form}
    return render(request, "placement/add_job.html", content)


@allowed_users(allowed_roles=['Placement_Cell'])
def recruiting(request):
    jobs = Job.objects.filter(status=0)
    curr = Job.objects.filter(status=0, apply_by__gt=date.today())
    placed = Job_user.objects.filter(status=3)
    hired = {}
    for job in jobs:
        count = 0
        for p in placed:
            # print(p.job_id,job)
            if p.job_id == job:
                count += 1
        hired[job] = count
    context = {"jobs": jobs, "curr": curr, "hired": hired}
    return render(request, "placement/recruiting.html", context)


@allowed_users(allowed_roles=['Placement_Cell'])
def recruited(request):
    jobs = Job.objects.filter(status=1)
    placed = Job_user.objects.filter(status=3)
    hired = {}
    for job in jobs:
        count = 0
        for p in placed:
            # print(p.job_id,job)
            if p.job_id == job:
                count += 1
        hired[job] = count
    context = {"jobs": jobs, "hired": hired}
    return render(request, "placement/recruited.html", context)


@allowed_users(allowed_roles=['Placement_Cell'])
def details(request, id, type):
    context = None
    if type == 1:
        jobs = Job.objects.get(id=id)
        applied = Job_user.objects.filter(job_id=id)
        # print(applied)
        context = {"details": jobs, "pay": "Salary", "applied": applied, "id": id, "type": type}
    elif type == 2:
        internships = Intership.objects.get(id=id)
        context = {"details": internships, "pay": "Stiped"}

    return render(request, "placement/details.html", context)


@allowed_users(allowed_roles=['Placement_Cell'])
def displayProfile(request, rollNo):
    student = Student.objects.get(roll_no=rollNo)
    user = User.objects.get(username=student.roll_no)
    name = user.first_name
    yearOfJoining = '20' + rollNo[0:2]
    branch = student.branch
    div = student.div
    studentId = rollNo[6:]
    exp = Add_exp.objects.filter(rollNo=rollNo)
    edu = Add_edu.objects.filter(roll_no=rollNo).order_by("degree")
    prev_deg = [edu.degree for edu in edu]

    curr_edu = CurrEdu.objects.filter(roll_no_curr=rollNo)
    certificate_list = Certificates.objects.filter(certificate_issued_to=rollNo)

    content = {'rollNo': rollNo, 'yearOfJoining': yearOfJoining, 'branch': branch, 'div': div,
               'studentId': studentId, 'edu_list': edu, 'exp_list': exp,
               'student_info': student, 'name': name, 'user': user,
               'prev_deg': prev_deg, 'certificate_list': certificate_list, 'curr_edu': curr_edu}
    return render(request, "placement/displayProfile.html", content)


@allowed_users(allowed_roles=['Placement_Cell'])
def status(request):
    data = json.loads(request.body)
    st = data["status"]
    id = data["id"]
    Job_user.objects.filter(id=id).update(status=st)

    return JsonResponse('Done', safe=False)


def send_email(request, id, comp):
    job = Job.objects.get(id=comp)
    job_user = Job_user.objects.get(id=id)
    student = Student.objects.get(roll_no=job_user.roll_no)

    if job_user.status == '3':

        send_accepted_email(student, job, request)
        Job_user.objects.filter(id=job_user.id).update(is_mail_send=True)
    elif job_user.status == '2':
        send_not_suitable_email(student, job, request)
    return redirect('/placement_cell/details/' + str(job.id) + "/1")


@allowed_users(allowed_roles=['Placement_Cell'])
def Update_Details(request, id):
    instance = Job.objects.get(id=id)
    form = JobForm(instance=instance)
    if request.method == "POST":
        form = JobForm(request.POST, instance=instance)
        print(form)
        if form.is_valid():
            form.save()
            Job.objects.filter(id=id).update(who_can_apply=who_can_apply_text(id))
            messages.success(request, 'Successfully Updated!')
            return redirect('/placement_cell/details/' + str(id) + "/1")
    content = {"form": form, "id": id}
    return render(request, "placement/update_details.html", content)


@allowed_users(allowed_roles=['Placement_Cell'])
def delete_details(request, id):
    job = Job.objects.get(id=id)
    job.delete()
    messages.success(request, "Successfully deleted!")
    return redirect('recruiting')


def student_details(request):
    students = Student.objects.all().order_by("branch")

    student_dict = {}
    for student in students:
        edu = Add_edu.objects.filter(roll_no=student)
        curr_edu = CurrEdu.objects.filter(roll_no_curr=student)
        certificate = Certificates.objects.filter(certificate_issued_to=student)
        experience = Add_exp.objects.filter(rollNo=student)
        user = User.objects.filter(username=student.roll_no)
        student_dict[student.roll_no] = [user, student, edu, curr_edu, certificate, experience]

    student_dict = sorted(student_dict.items())
    content = {'student_dict': student_dict}
    return render(request, 'placement/student_details.html', content)
