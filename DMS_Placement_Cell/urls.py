from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.index, name='placementIndex'),
    path("add_intership/",views.add_intership,name="add_intership"),
    path("add_job/",views.add_job,name="add_job"),
    path("form_intership",views.form_intership,name="form_intership"),
    # path("form_job",views.form_job,name="form_job"),
    path("recruiting/",views.recruiting,name="recruiting"),
    path("recruited/",views.recruited,name="recruited"),
    path("details/<int:id>/<int:type>/",views.details,name="details"),
    path("displayProfile/<slug:rollNo>/",views.displayProfile,name="displayProfile"),
    path("status/",views.status,name="status"),
]