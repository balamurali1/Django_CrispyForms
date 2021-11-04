"""
WSGI config for gs74_CreateRegistration_Form_Using_UserCreationForm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs74_CreateRegistration_Form_Using_UserCreationForm.settings')

application = get_wsgi_application()
