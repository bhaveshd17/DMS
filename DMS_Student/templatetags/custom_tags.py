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
