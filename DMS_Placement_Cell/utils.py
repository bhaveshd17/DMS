from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from typing import LiteralString
from dataclasses import dataclass

from DMS_Student.models import Job

def send_accepted_email(student, job, request):
    try:
        current_site = get_current_site(request)
        email_subject: LiteralString = "Job Offer"
        email_body = render_to_string("placement/accept.html", {
            'student': student,
            'job': job,
        })

        email = EmailMessage(
            subject=email_subject,
            body=email_body,
            from_email=settings.EMAIL_HOST_USER,
            to=[student.gmail]
        )
        email.fail_silently = False
        email.content_subtype = 'html'
        email.send()
    except Exception as e:
        e.add_note("Failed to send accepted email to student.")
        raise

def send_not_suitable_email(student, job, request):
    try:
        current_site = get_current_site(request)
        email_subject: LiteralString = "Job Status."
        email_body = render_to_string("placement/not_suitable.html", {
            'student': student,
            'job': job,
        })

        email = EmailMessage(
            subject=email_subject,
            body=email_body,
            from_email=settings.EMAIL_HOST_USER,
            to=[student.gmail]
        )
        email.fail_silently = False
        email.content_subtype = 'html'
        email.send()
    except Exception as e:
        e.add_note("Failed to send not suitable email to student.")
        raise

@dataclass
class JobCriteria:
    aggregate_sgpi: str
    ssc_percentage: str
    hsc_d_percentage: str
    live_kt: str
    dead_kt: str
    drop: str

def who_can_apply_text(job: Job) -> str:
    criteria = JobCriteria(
        aggregate_sgpi=job.aggregate_sgpi,
        ssc_percentage=job.ssc_percentage,
        hsc_d_percentage=job.hsc_d_percentage,
        live_kt=job.live_kt,
        dead_kt=job.dead_kt,
        drop=job.drop
    )
    
    text = ""
    if criteria.aggregate_sgpi != "NA":
        text += f"<li class='text-left'>Minimum {criteria.aggregate_sgpi} SGPI required</li>"
    if criteria.ssc_percentage != "NA":
        text += f"<li class='text-left'>Minimum {criteria.ssc_percentage} % of 10th required </li>"
    if criteria.hsc_d_percentage != "NA":
        text += f"<li class='text-left'>Minimum {criteria.hsc_d_percentage} % of 12/diploma required</li>"
    if criteria.live_kt != "NA":
        text += f"<li class='text-left'>Minimum {criteria.live_kt} Live KT </li>"
    if criteria.dead_kt != "NA":
        text += f"<li class='text-left'>Minimum {criteria.dead_kt} Dead KT</li>"
    if criteria.drop != "0":
        text += f"<li class='text-left'>Minimum {criteria.drop} year drop</li>"
    if text == "":
        text = "No Criteria"
    return text
