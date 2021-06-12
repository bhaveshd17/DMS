from . import views
from django.urls import path

urlpatterns = [
    path('student/', views.index, name='index')
]