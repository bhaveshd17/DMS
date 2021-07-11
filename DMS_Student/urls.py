from os import name
from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.handleLogin, name='login'),
    path('logout/', views.handelLogout, name='logout'),
    path('register/',views.register,name="register"),
    path('activate_user/<uidb64>/<token>/',views.activate_user,name="activate_user"),
    path('otp/',views.otp,name="otp"),

    
    path('student/', views.index, name='index'),
    path('student/internship', views.internship, name='internship'),
    path('student/internshipFilter', views.internshipFilter, name="internshipFilter"),
    path('student/jobFilter', views.jobFilter, name="jobFilter"),
    path('student/preplacement', views.preplacement, name='preplacement'),
    path('student/job', views.job, name='job'),
    path('student/all_job', views.all_job, name='all_job'),
    path('student/details/<int:id>/<int:type>', views.details, name='details'),
    path('student/apply/', views.apply, name='apply'),
    path('student/search', views.search, name='search'),

    path('student/profile',views.profile,name='profile'),
    path('student/UpdateSkills',views.UpdateSkills,name='UpdateSkills'),

    path('student/addEdu',views.add_education,name="addEdu"),
    path('student/updateEdu/<int:pk>/', views.update_education,name="updateEdu"),
    path('student/deleteEdu/<int:pk>/', views.delete_education,name="deleteEdu"),

    path('student/addExp',views.add_experience,name="addExp"),
    path('student/updateExp/<int:pk>/', views.update_experience, name="updateExp"),
    path('student/deleteExp/<int:pk>/', views.delete_experience, name="deleteExp"),

    path('student/add_current_education', views.add_curr_education, name="addCurrEdu"),
    path('student/update_current_education/<int:pk>/', views.update_curr_education, name="updateCurrEdu"),
    path('student/add_current_education/<int:pk>/', views.delete_curr_education, name="deleteCurrEdu"),

    path('student/add_certificates', views.add_certificates, name='addCertificates'),
    path('student/update_certificate/<int:pk>', views.update_certificate, name='updateCertificate'),
    path('student/delete_certificates/<int:pk>/', views.delete_certificates, name='deleteCertificates'),

    path('student/userApplication',views.userApplication,name="userApplication"),
]