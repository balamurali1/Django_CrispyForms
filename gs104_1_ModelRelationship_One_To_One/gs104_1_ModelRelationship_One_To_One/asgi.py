"""
ASGI config for gs104_1_ModelRelationship_One_To_One project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs104_1_ModelRelationship_One_To_One.settings')

application = get_asgi_application()