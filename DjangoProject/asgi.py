"""
ASGI config for DjangoProject project.
Asynchronous Server Gateway Interface (ASGI) application with ASGI-compatible web servers.
ASGI is the emerging Python standard for asynchronous web servers and applications
It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject.settings')

application = get_asgi_application()
