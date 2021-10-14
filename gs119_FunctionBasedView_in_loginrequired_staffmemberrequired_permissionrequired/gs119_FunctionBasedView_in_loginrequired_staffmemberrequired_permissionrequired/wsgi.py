"""
WSGI config for gs119_FunctionBasedView_in_loginrequired_staffmemberrequired_permissionrequired project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs119_FunctionBasedView_in_loginrequired_staffmemberrequired_permissionrequired.settings')

application = get_wsgi_application()
