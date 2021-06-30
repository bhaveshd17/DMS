from django.db.models import fields
from django.forms import ModelForm
from DMS_Student.models import  Intership,Job

class IntershipForm(ModelForm):
    class Meta:
        model=Intership
        fields='__all__'

class JobForm(ModelForm):
    class Meta:
        model=Job
        fields='__all__'

