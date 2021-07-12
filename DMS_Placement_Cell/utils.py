from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_str,force_text,DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

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