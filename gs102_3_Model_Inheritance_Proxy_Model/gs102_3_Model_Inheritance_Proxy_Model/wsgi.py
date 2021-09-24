"""
WSGI config for gs102_3_Model_Inheritance_Proxy_Model project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs102_3_Model_Inheritance_Proxy_Model.settings')

application = get_wsgi_application()
