from django.db.models import fields
from django.forms import ModelForm
from DMS_Student.models import Intership, Job

class IntershipForm(ModelForm):
    class Meta:
        model = Intership
        fields = '__all__'

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

# Note: The original code does not contain any exception handling that would require the use of exception groups.
# Therefore, no changes related to exception handling are necessary for compatibility with Python 3.11.
