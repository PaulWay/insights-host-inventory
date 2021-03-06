"""
WSGI config for insights project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import logging

from django.core.wsgi import get_wsgi_application

logging.basicConfig()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "insights.settings")

application = get_wsgi_application()
