from . import views
from django.urls import path

urlpatterns = [
    path('student/', views.index, name='index'),
    path('student/internship', views.internship, name='internship'),
    path('student/preplacement', views.preplacement, name='preplacement'),
    path('student/job', views.job, name='job'),
    path('student/details/<int:id>/<int:type>', views.details, name='details'),
]