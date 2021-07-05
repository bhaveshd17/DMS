from django import template
register = template.Library()

@register.filter(name='cgpa_percentage_conversion')
def cgpa_percentage_conversion(cgpa):
    percentage = cgpa*7.1 + 11
    return round(percentage, 2)
