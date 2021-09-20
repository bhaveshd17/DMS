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
    resource_class  =   StudentResource
admin.site.register(Student,StudentAdmin)

class Add_eduAdmin(ImportExportModelAdmin):
    resource_class  =   Add_eduResource
admin.site.register(Add_edu,Add_eduAdmin)

class CurrEduAdmin(ImportExportModelAdmin):
    resource_class=CurrEduResource
admin.site.register(CurrEdu,CurrEduAdmin)

class Job_userAdmin(ImportExportModelAdmin):
    resource_class=Job_userResource

class JobAdmin(ImportExportModelAdmin):
    resource_class=JobResource 
admin.site.register(Job,JobAdmin)
admin.site.register(Job_user,Job_userAdmin)
admin.site.register(Add_exp)
admin.site.register(Intership)
admin.site.register(Int_user)
admin.site.register(Mock_test)
admin.site.register(Certificates)


