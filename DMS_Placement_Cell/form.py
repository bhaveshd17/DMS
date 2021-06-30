from django.forms import ModelForm
from DMS_Student.models import  Intership,Job

class IntershipForm(ModelForm):
    class Meta:
        model=Intership
        fields='__all__'

