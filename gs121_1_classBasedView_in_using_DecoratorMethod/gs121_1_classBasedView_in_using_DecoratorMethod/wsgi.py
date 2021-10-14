"""
WSGI config for gs121_1_classBasedView_in_using_DecoratorMethod project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs121_1_classBasedView_in_using_DecoratorMethod.settings')

application = get_wsgi_application()
