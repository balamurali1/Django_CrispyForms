"""
ASGI config for gs102_3_Model_Inheritance_Proxy_Model project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs102_3_Model_Inheritance_Proxy_Model.settings')

application = get_asgi_application()
