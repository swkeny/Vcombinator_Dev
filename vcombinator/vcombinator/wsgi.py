"""
WSGI config for vcombinator project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vcombinator.vcombinator.settings")

sys.path.append('/opt/python/run/venv/lib/python3.4/site-packages')
from django.core.wsgi import get_wsgi_application


application = get_wsgi_application()
