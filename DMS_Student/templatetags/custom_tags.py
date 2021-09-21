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
    if(salary[0]=='[' and salary[-1]==']'):
        salary=salary[1:len(salary)-1]
    
    salary=[float(i) for i in salary.split(",")]
    if min(salary)/100000==max(salary)/100000:return min(salary)/100000
    return str(min(salary)/100000)+" - "+str(max(salary)/100000)