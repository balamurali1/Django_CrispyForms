"""
ASGI config for gs76_ChangePassword_with_OldPassword_and_without_Oldpassword project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs76_ChangePassword_with_OldPassword_and_without_Oldpassword.settings')

application = get_asgi_application()
