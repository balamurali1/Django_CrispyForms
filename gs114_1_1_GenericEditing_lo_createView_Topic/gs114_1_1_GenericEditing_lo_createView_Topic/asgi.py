"""
ASGI config for gs114_1_1_GenericEditing_lo_createView_Topic project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs114_1_1_GenericEditing_lo_createView_Topic.settings')

application = get_asgi_application()
