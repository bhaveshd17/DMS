from django.forms import ModelForm
from .models import  Student, Add_edu

class SkillsForm(ModelForm):
    class Meta:
        model=Student
        fields=['skills']

class AddEduForm(ModelForm):
    class Meta:
        model=Add_edu
        fields='__all__'
