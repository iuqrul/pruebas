#encoding:utf-8
import os
import sys
from os.path import abspath, dirname, join, normpath
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(os.path.dirname(BASE_DIR),
                             'lib', 'python2.7', 'site-packages'))


DJANGO_ROOT = dirname(dirname(abspath(__file__)))
SITE_HTDOCS = normpath(join(DJANGO_ROOT, '../htdocs'))

STATIC_ROOT = normpath(join(SITE_HTDOCS, 'static'))
STATIC_URL = '/static/'
DEBUG = True
TEMPLATE_DEBUG = DEBUG

TIME_ZONE = 'Europe/Madrid'
LANGUAGE_CODE = 'es'
USE_I18N = True
USE_L10N = True
USE_TZ = True

with open(os.path.join(os.path.dirname(__file__), 'secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',


)


INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'south',
    'django_extensions',
    'rest_framework',

    'pipeline',
    'raven.contrib.django.raven_compat',
    'bootstrap3',

    'tvhoradada',
    'clientes',
    'corsheaders',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

STATICFILES_DIRS = (
    join(DJANGO_ROOT, 'bower_components'),
)


from .pipeline import *
from .rest import *

ROOT_URLCONF = 'tvhoradada.urls'


LOGIN_URL="/login"



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

ALLOWED_HOSTS = ['*']
#SESSION_COOKIE_AGE = 900

CORS_ORIGIN_ALLOW_ALL = True
#CORS_ALLOW_CREDENTIALS = True
#CORS_ALLOW_METHODS
