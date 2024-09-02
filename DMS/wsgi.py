"""
WSGI config for DMS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DMS.settings')

application = get_wsgi_application()

# Note: The original code does not handle multiple exceptions, and the provided instructions
# do not specify any exceptions to handle. Therefore, no changes are necessary for exception handling.
