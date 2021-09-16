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
#     list_display=("username","first_name","email","password")

# class StudentResource(resources.ModelResource):

#     class Meta:
#         model =Student




class StudentAdmin(ImportExportModelAdmin):
    resource_class  =   StudentResource
admin.site.register(Student,StudentAdmin)

class Add_eduAdmin(ImportExportModelAdmin):
    resource_class  =   Add_eduResource
admin.site.register(Add_edu,Add_eduAdmin)

class CurrEduAdmin(ImportExportModelAdmin):
    resource_class=CurrEduResource
admin.site.register(CurrEdu,CurrEduAdmin)

admin.site.register(Add_exp)
admin.site.register(Intership)
admin.site.register(Int_user)
admin.site.register(Job)
admin.site.register(Job_user)
admin.site.register(Mock_test)
admin.site.register(Certificates)


