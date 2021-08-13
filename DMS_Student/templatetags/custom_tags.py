from django import template
register = template.Library()

@register.filter(name='cgpa_percentage_conversion')
def cgpa_percentage_conversion(cgpa):
    percentage = cgpa*7.1 + 11
    return round(percentage, 2)

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