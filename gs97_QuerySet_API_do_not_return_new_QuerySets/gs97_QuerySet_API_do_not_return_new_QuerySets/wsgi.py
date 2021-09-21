"""
WSGI config for gs97_QuerySet_API_do_not_return_new_QuerySets project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs97_QuerySet_API_do_not_return_new_QuerySets.settings')

application = get_wsgi_application()
