from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.index, name='placementIndex'),
    path("add_intership/",views.add_intership,name="add_intership"),
    path("add_job/",views.add_job,name="add_job"),
]