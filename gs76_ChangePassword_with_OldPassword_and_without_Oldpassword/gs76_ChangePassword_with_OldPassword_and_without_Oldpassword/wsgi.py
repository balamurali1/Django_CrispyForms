"""
WSGI config for gs76_ChangePassword_with_OldPassword_and_without_Oldpassword project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs76_ChangePassword_with_OldPassword_and_without_Oldpassword.settings')

application = get_wsgi_application()
