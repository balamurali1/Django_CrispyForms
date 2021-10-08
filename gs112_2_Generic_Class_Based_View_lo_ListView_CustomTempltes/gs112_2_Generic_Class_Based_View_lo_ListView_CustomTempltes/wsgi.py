"""
WSGI config for gs112_2_Generic_Class_Based_View_lo_ListView_CustomTempltes project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs112_2_Generic_Class_Based_View_lo_ListView_CustomTempltes.settings')

application = get_wsgi_application()
