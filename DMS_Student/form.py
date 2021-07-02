from django.forms import ModelForm
from .models import  Student, Add_edu, Add_exp

class SkillsForm(ModelForm):
    class Meta:
        model=Student
        fields=['skills']

class AddEduForm(ModelForm):
    class Meta:
        model=Add_edu
        fields='__all__'

class AddExpForm(ModelForm):
    class Meta:
        model=Add_exp
        fields='__all__'
