from django.db import models
from django.forms import ModelForm
from .models import Student, Add_edu, Add_exp, CurrEdu, Certificates
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from typing import Self

class SkillsForm(ModelForm):
    class Meta:
        model = Student
        fields = ['skills']

class AddEduForm(ModelForm):
    class Meta:
        model = Add_edu
        fields = '__all__'

class AddExpForm(ModelForm):
    class Meta:
        model = Add_exp
        fields = '__all__'

class CurrEduForm(ModelForm):
    class Meta:
        model = CurrEdu
        fields = '__all__'

class CertificateForm(ModelForm):
    class Meta:
        model = Certificates
        fields = '__all__'

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "email", "password1", "password2"]

# No exception handling code is present in the original file, so no changes are needed for exception groups.
