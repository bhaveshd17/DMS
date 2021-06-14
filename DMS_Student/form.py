from django.forms import ModelForm
from .models import  Student

class SkillsForm(ModelForm):
    class Meta:
        model=Student
        fields=['skills']

