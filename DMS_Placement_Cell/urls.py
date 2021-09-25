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
    path("send_email/<id>/<comp>/",views.send_email,name="send_email"),
    path("update_details/<int:id>/",views.Update_Details,name="Update_Details"),
    path("delete_details/<int:id>",views.delete_details,name="delete_details"),
    path("student_details/", views.student_details, name="student_details"),
    path("sector/",views.sector,name="sector"),
    path("analyssis/companyWise",views.companyWise,name="companyWise"),
    
    path("analysis/ctcwise/", views.ctcWise, name='ctcWise'),
    path("analysis/gender_ratio/", views.gender_ratio, name='gender_ratio'),
]