"""
WSGI config for gs98_QuerySet_API_Field_Lookups project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs98_QuerySet_API_Field_Lookups.settings')

application = get_wsgi_application()
