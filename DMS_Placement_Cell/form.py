from django.db.models import fields
from django.forms import ModelForm
from DMS_Student.models import Intership, Job
from typing import Self, LiteralString
from dataclasses import dataclass

@dataclass
class IntershipForm(ModelForm):
    class Meta:
        model = Intership
        fields = '__all__'

    def save(self, *args: LiteralString, **kwargs: LiteralString) -> Self:
        return super().save(*args, **kwargs)

@dataclass
class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

    def save(self, *args: LiteralString, **kwargs: LiteralString) -> Self:
        return super().save(*args, **kwargs)

# Note: The original code does not contain any exception handling that would require the use of exception groups.
# Therefore, no changes related to exception handling are necessary for compatibility with Python 3.11.
