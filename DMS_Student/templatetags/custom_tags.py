import math
from django import template
import datetime

register = template.Library()

@register.filter(name='cgpa_percentage_conversion')
def cgpa_percentage_conversion(cgpa):
    percentage = cgpa * 7.1 + 11
    return round(percentage, 2)

@register.filter(name='date_format')
def date_formate(value):
    string = f"{value.day}-{value.month}-{value.year}"
    return string

@register.filter(name='to_int')
def to_int(value):
    return int(value)

@register.filter(name='disability')
def disability(value):
    return 'yes' if value else 'NA'

@register.simple_tag
def marks_to_percentage(marks, subject):
    try:
        percentage = int(marks) / int(subject)
    except (ValueError, ZeroDivisionError) as e:
        e.add_note("Ensure 'marks' and 'subject' are valid integers and 'subject' is not zero.")
        raise ValueError(f"Error calculating percentage: {e}") from e
    return percentage

@register.filter(name='sal')
def sal(salary):
    salary = [float(i) for i in salary.split(",")]
    if min(salary) == max(salary):
        return min(salary) / 100000
    return f"{min(salary) / 100000}-{max(salary) / 100000}"

@register.filter(name='average_sal')
def average_sal(data):
    ls = [int(value[0]) for d in data for key, value in d.items()]
    return str(math.ceil(sum(ls) / len(ls)))

@register.filter(name='no_placed')
def no_placed(data):
    ls = [value[1] for d in data for key, value in d.items()]
    return str(sum(ls))

@register.filter(name='data')
def data(dic):
    return [value['grand_total'] for key, value in dic.items()]

@register.filter(name='total_count')
def total_count(dic):
    gen_dic = {"male": [], "female": []}
    for key, value in dic.items():
        gen_dic["male"].append(value['male'])
        gen_dic["female"].append(value['female'])
    return [sum(gen_dic['male']), sum(gen_dic['female'])]

@register.filter(name='total_count_placed')
def total_count_placed(dic):
    gen_dic_placed = {"male": [], "female": []}
    for key, value in dic.items():
        gen_dic_placed["male"].append(value['pmale'])
        gen_dic_placed["female"].append(value['pfemale'])
    return [sum(gen_dic_placed['male']), sum(gen_dic_placed['female'])]

@register.filter(name='dictAccess')
def dictAccess(value, key):
    return value[str(key)]

@register.simple_tag
def totalOffer(value, labelSector, sector):
    return value[labelSector.index(sector)]

@register.filter(name="dictToList")
def dictToList(sectorCompany):
    return list(sectorCompany.values())

@register.filter(name="dictKeys")
def dictKeys(sectorCompany):
    return list(sectorCompany.keys())

@register.filter(name="offer_sal")
def offer_sal(value):
    return [i.salary for i in value][0]

# @register.filter(name="companyWiseData")
# def companyWiseData(sectorCompany):
#     return list(sectorCompany.values()).sort()

# @register.filter(name="companyWiseLabel")
# def companyWiseLabel(sectorCompany):
#     return list(sectorCompany.keys())
