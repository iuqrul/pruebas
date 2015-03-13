 #!/usr/bin/python
import sys, os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

# For virtualenv
PROJECT_LIBS = os.path.join(PROJECT_ROOT, "lib", "python2.7", "site-packages")
sys.path.insert(1, PROJECT_LIBS)

PROJECT_LIBS = os.path.join(PROJECT_ROOT, "lib", "python2.6", "site-packages")
sys.path.insert(1, PROJECT_LIBS)


os.environ['DJANGO_SETTINGS_MODULE'] = "local_settings"

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
