"""
ASGI config for gs112_Generic_Class_BasedView_lo_ListView project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs112_Generic_Class_BasedView_lo_ListView.settings')

application = get_asgi_application()
