#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # For virtualenv
    PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
    PROJECT_LIBS = os.path.join(PROJECT_ROOT, "lib", "python2.7", "site-packages")
    sys.path.insert(1, PROJECT_LIBS)
    PROJECT_LIBS = os.path.join(PROJECT_ROOT, "lib", "python2.6", "site-packages")
    sys.path.insert(1, PROJECT_LIBS)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "local_settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
