import math
from django import template
import datetime
from typing import Any, Dict, List, Tuple

register = template.Library()

@register.filter(name='cgpa_percentage_conversion')
def cgpa_percentage_conversion(cgpa: float) -> float:
    percentage = cgpa * 7.1 + 11
    return round(percentage, 2)

@register.filter(name='date_format')
def date_formate(value: datetime.date) -> str:
    string = f"{value.day}-{value.month}-{value.year}"
    return string

@register.filter(name='to_int')
def to_int(value: Any) -> int:
    return int(value)

@register.filter(name='disability')
def disability(value: bool) -> str:
    return 'yes' if value else 'NA'

@register.simple_tag
def marks_to_percentage(marks: int, subject: int) -> float:
    try:
        percentage = int(marks) / int(subject)
    except (ValueError, ZeroDivisionError) as e:
        e.add_note("Ensure 'marks' and 'subject' are valid integers and 'subject' is not zero.")
        raise ValueError(f"Error calculating percentage: {e}") from e
    return percentage

@register.filter(name='sal')
def sal(salary: str) -> str:
    salary_list = [float(i) for i in salary.split(",")]
    if min(salary_list) == max(salary_list):
        return str(min(salary_list) / 100000)
    return f"{min(salary_list) / 100000}-{max(salary_list) / 100000}"

@register.filter(name='average_sal')
def average_sal(data: List[Dict[str, Tuple[int, int]]]) -> str:
    ls = [int(value[0]) for d in data for key, value in d.items()]
    return str(math.ceil(sum(ls) / len(ls)))

@register.filter(name='no_placed')
def no_placed(data: List[Dict[str, Tuple[int, int]]]) -> str:
    ls = [value[1] for d in data for key, value in d.items()]
    return str(sum(ls))

@register.filter(name='data')
def data(dic: Dict[str, Dict[str, int]]) -> List[int]:
    return [value['grand_total'] for key, value in dic.items()]

@register.filter(name='total_count')
def total_count(dic: Dict[str, Dict[str, int]]) -> List[int]:
    gen_dic = {"male": [], "female": []}
    for key, value in dic.items():
        gen_dic["male"].append(value['male'])
        gen_dic["female"].append(value['female'])
    return [sum(gen_dic['male']), sum(gen_dic['female'])]

@register.filter(name='total_count_placed')
def total_count_placed(dic: Dict[str, Dict[str, int]]) -> List[int]:
    gen_dic_placed = {"male": [], "female": []}
    for key, value in dic.items():
        gen_dic_placed["male"].append(value['pmale'])
        gen_dic_placed["female"].append(value['pfemale'])
    return [sum(gen_dic_placed['male']), sum(gen_dic_placed['female'])]

@register.filter(name='dictAccess')
def dictAccess(value: Dict[str, Any], key: str) -> Any:
    return value[str(key)]

@register.simple_tag
def totalOffer(value: List[int], labelSector: List[str], sector: str) -> int:
    return value[labelSector.index(sector)]

@register.filter(name="dictToList")
def dictToList(sectorCompany: Dict[str, Any]) -> List[Any]:
    return list(sectorCompany.values())

@register.filter(name="dictKeys")
def dictKeys(sectorCompany: Dict[str, Any]) -> List[str]:
    return list(sectorCompany.keys())

@register.filter(name="offer_sal")
def offer_sal(value: List[Any]) -> float:
    return [i.salary for i in value][0]

# @register.filter(name="companyWiseData")
# def companyWiseData(sectorCompany: Dict[str, Any]) -> List[Any]:
#     return list(sectorCompany.values()).sort()

# @register.filter(name="companyWiseLabel")
# def companyWiseLabel(sectorCompany: Dict[str, Any]) -> List[str]:
#     return list(sectorCompany.keys())
