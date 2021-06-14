from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.handleLogin, name='login'),
    path('logout/', views.handelLogout, name='logout'),
    path('student/', views.index, name='index'),
    path('student/internship', views.internship, name='internship'),
    path('student/preplacement', views.preplacement, name='preplacement'),
    path('student/job', views.job, name='job'),
    path('student/details/<int:id>/<int:type>', views.details, name='details'),
    path('student/profile',views.profile,name='profile'),
    path('student/UpdateSkills',views.UpdateSkills,name='UpdateSkills'),
]