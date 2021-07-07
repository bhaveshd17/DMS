from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import  Student, Add_edu, Add_exp, FE, SE, TE, BE, Certificates
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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

class FeForm(ModelForm):
    class Meta:
        model=FE
        fields='__all__'

class SeForm(ModelForm):
    class Meta:
        model=SE
        fields='__all__'

class TeForm(ModelForm):
    class Meta:
        model=TE
        fields='__all__'

class BeForm(ModelForm):
    class Meta:
        model=BE
        fields='__all__'

class CertificateForm(ModelForm):
    class Meta:
        model=Certificates
        fields='__all__'

class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","first_name","email","password1","password2"]