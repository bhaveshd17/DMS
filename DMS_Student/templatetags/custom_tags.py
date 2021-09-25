import math

from django import template
import datetime
register = template.Library()

@register.filter(name='cgpa_percentage_conversion')
def cgpa_percentage_conversion(cgpa):
    percentage = cgpa*7.1 + 11
    return round(percentage, 2)

@register.filter(name='date_format')
def date_formate(value):
    string = str(value.day)+'-'+str(value.month)+'-'+str(value.year)
    return string

@register.filter(name='to_int')
def to_int(value):
    return int(value)

@register.filter(name='disability')
def disability(value):
    if value == True:
        text = 'yes'
    else:
        text = 'NA'
    return text

@register.simple_tag
def marks_to_percentage(marks, subject):
    try:
        percentage = int(marks)/int(subject)
    except:
        percentage=0
    return percentage

@register.filter(name='sal')
def sal(salary):
    salary=[float(i) for i in salary.split(",")]
    if min(salary)==max(salary):return min(salary)/100000
    return str(min(salary)/100000)+"-"+str(max(salary)/100000)

@register.filter(name='average_sal')
def average_sal(data):
    ls = []
    for d in data:
        for key, value in d.items():
            ls.append(int(value[0]))
    return str(math.ceil(sum(ls)/len(ls)))

@register.filter(name='no_placed')
def no_placed(data):
    ls = []
    for d in data:
        for key, value in d.items():
            ls.append(value[1])
    return str(sum(ls))

@register.filter(name='data')
def data(dic):
    ls = []
    for key, value in dic.items():
        ls.append(value['grand_total'])
    return ls

@register.filter(name='total_count')
def total_count(dic):
    gen_dic = {"male":[], "female":[]}
    for key, value in dic.items():
        gen_dic["male"].append(value['male'])
        gen_dic["female"].append(value['female'])
    return [sum(gen_dic['male']), sum(gen_dic['female'])]

@register.filter(name='total_count_placed')
def total_count_placed(dic):
    gen_dic_placed = {"male":[], "female":[]}
    for key, value in dic.items():
        gen_dic_placed["male"].append(value['pmale'])
        gen_dic_placed["female"].append(value['pfemale'])
    return [sum(gen_dic_placed['male']), sum(gen_dic_placed['female'])]

@register.filter(name='dictAccess')
def dictAccess(value,key):
    return value[str(key)]

@register.simple_tag
def totalOffer(value,labelSector,sector):
    print("Working")
    return value[labelSector.index(sector)]

@register.filter(name="dictToList")
def dictToList(sectorCompany):
    return list(sectorCompany.values())

@register.filter(name="dictKeys")
def dictKeys(sectorCompany):
    return list(sectorCompany.keys())