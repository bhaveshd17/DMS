from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin
from import_export import resources
from .resources import *

# admin.site.unregister(User)
# @admin.register(User)
# class UserAdmin(ImportExportActionModelAdmin):
#     list_display=("username","first_name","email")

class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource

    @classmethod
    def create(cls) -> Self:
        return cls()

admin.site.register(Student, StudentAdmin)

class Add_eduAdmin(ImportExportModelAdmin):
    resource_class = Add_eduResource

    @classmethod
    def create(cls) -> Self:
        return cls()

admin.site.register(Add_edu, Add_eduAdmin)

class CurrEduAdmin(ImportExportModelAdmin):
    resource_class = CurrEduResource

    @classmethod
    def create(cls) -> Self:
        return cls()

admin.site.register(CurrEdu, CurrEduAdmin)

class Job_userAdmin(ImportExportModelAdmin):
    resource_class = Job_userResource

    @classmethod
    def create(cls) -> Self:
        return cls()

class JobAdmin(ImportExportModelAdmin):
    resource_class = JobResource

    @classmethod
    def create(cls) -> Self:
        return cls()

admin.site.register(Job, JobAdmin)
admin.site.register(Job_user, Job_userAdmin)
admin.site.register(Add_exp)
admin.site.register(Intership)
admin.site.register(Int_user)
admin.site.register(Mock_test)
admin.site.register(Certificates)

# Note: Python 3.11 introduces fine-grained error locations in tracebacks by default.
# No specific code changes are required here for compatibility with Python 3.11.

# No exception handling code is present in this file that requires the use of exception groups.
