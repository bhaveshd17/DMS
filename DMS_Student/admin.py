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
    # list_display = ["roll_no", "phone", "skills", "age", "gender", "branch", "div", "corresponding_address", "permanent_address", "date_of_birth", "gmail", "residence_phone", "pan_card_no", "aadhar_no", "passport_no", "year_of_graduation", "disability", "type_of_disability", "father_name", "mother_name", "father_occupation", "mother_occupation", "co_curriculum_activities", "extra_curriculum_activities", "hobbies", "profile_photo", "resume", "facebook", "linkdin", "github", "other", "is_email_verified"]
  
admin.site.register(Student,StudentAdmin)

class Add_eduAdmin(ImportExportModelAdmin):
    resource_class  =   Add_eduResource
admin.site.register(Add_edu,Add_eduAdmin)
admin.site.register(Add_exp)
admin.site.register(Intership)
admin.site.register(Int_user)
admin.site.register(Job)
admin.site.register(Job_user)
admin.site.register(Mock_test)
admin.site.register(CurrEdu)
admin.site.register(Certificates)


