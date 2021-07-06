from django.forms import ModelForm
from .models import  Student, Add_edu, Add_exp, FE, SE, TE, BE, Certificates

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