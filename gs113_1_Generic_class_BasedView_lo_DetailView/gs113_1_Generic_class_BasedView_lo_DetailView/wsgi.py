"""
WSGI config for gs113_1_Generic_class_BasedView_lo_DetailView project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs113_1_Generic_class_BasedView_lo_DetailView.settings')

application = get_wsgi_application()
