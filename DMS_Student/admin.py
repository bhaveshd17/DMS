from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

admin.site.register(Student)
admin.site.register(Add_edu)
admin.site.register(Add_exp)
admin.site.register(Intership)
admin.site.register(Int_user)
admin.site.register(Job)
admin.site.register(Job_user)
admin.site.register(Mock_test)
admin.site.register(CurrEdu)
admin.site.register(Certificates)


