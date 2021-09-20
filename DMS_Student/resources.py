from import_export import resources
from .models import *

class StudentResource(resources.ModelResource):

    class Meta:
        model   =   Student
        import_id_fields = ['roll_no']

class Add_eduResource(resources.ModelResource):

    class Meta:
        model   =   Add_edu
        # import_id_fields = ['roll_no']


class CurrEduResource(resources.ModelResource):

    class Meta:
        model   =   CurrEdu

class Job_userResource(resources.ModelResource):

    class Meta:
        model   =   Job_user

class JobResource(resources.ModelResource):

    class Meta:
        model   =   Job