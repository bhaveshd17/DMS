"""
ASGI config for DMS project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Set the default settings module for the 'asgi' application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DMS.settings')

# Get the ASGI application
application = get_asgi_application()

# Python 3.11 compatibility: Utilize fine-grained error locations in tracebacks
# This is automatically handled by Python 3.11's improved error reporting
