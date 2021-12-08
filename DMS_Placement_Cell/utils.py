from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from DMS_Student.models import Job






def send_accepted_email(student,job,request):
    current_site=get_current_site(request)
    email_subject="Job Offer"
    email_body=render_to_string("placement/accept.html",{
        'student':student,
        'job':job,
    })

    email=EmailMessage(subject=email_subject,body=email_body,
    from_email=settings.EMAIL_HOST_USER,
    to=[student.gmail]
    )
    email.fail_silently = False
    email.content_subtype = 'html'
    email.send()

def send_not_suitable_email(student,job,request):
    current_site=get_current_site(request)
    email_subject="Job Status."
    email_body=render_to_string("placement/not_suitable.html",{
        'student':student,
        'job':job,
    })

    email=EmailMessage(subject=email_subject,body=email_body,
    from_email=settings.EMAIL_HOST_USER,
    to=[student.gmail]
    )
    
    email.fail_silently = False
    email.content_subtype = 'html'
    email.send()


def who_can_apply_text(job):
    text = ""
    if job.aggregate_sgpi != "NA":
        text = text + f"<li class='text-left'>Minimum {job.aggregate_sgpi} SGPI required</li>"
    if job.ssc_percentage != "NA":
        text = text + f"<li class='text-left'>Minimum {job.ssc_percentage} % of 10th required </li>"
    if job.hsc_d_percentage != "NA":
        text = text + f"<li class='text-left'>Minimum {job.hsc_d_percentage} % of 12/diploma required</li>"
    if job.live_kt != "NA":
        text = text + f"<li class='text-left'>Minimum {job.live_kt} Live KT </li>"
    if job.dead_kt != "NA":
        text = text + f"<li class='text-left'>Minimum {job.dead_kt} Dead KT</li>"
    if job.drop != "0":
        text = text + f"<li class='text-left'>Minimum {job.drop} year drop</li>"
    if text == "":
        text = "No Criteria"
    return text