import os

from django.core.wsgi import get_wsgi_application

# GETTING-STARTED: change 'myproject' to your project name:
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

application = get_wsgi_application()