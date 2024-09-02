from import_export import resources
from .models import *

class StudentResource(resources.ModelResource):

    class Meta:
        model = Student
        import_id_fields = ['roll_no']

    def get_instance(self) -> Self:
        return self

class Add_eduResource(resources.ModelResource):

    class Meta:
        model = Add_edu
        # import_id_fields = ['roll_no']

    def get_instance(self) -> Self:
        return self

class CurrEduResource(resources.ModelResource):

    class Meta:
        model = CurrEdu

    def get_instance(self) -> Self:
        return self

class Job_userResource(resources.ModelResource):

    class Meta:
        model = Job_user

    def get_instance(self) -> Self:
        return self

class JobResource(resources.ModelResource):

    class Meta:
        model = Job

    def get_instance(self) -> Self:
        return self

# Python 3.11 compatibility is ensured by default as the code does not use any deprecated features or syntax.
# If debugging errors, Python 3.11 provides fine-grained error locations in tracebacks by default.
