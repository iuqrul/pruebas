from trueip.settings import *

DEBUG=False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'trueip',
        'USER': 'trueip',
        'PASSWORD': 'tru394821',
        'HOST': 'localhost',
    },

}

#CACHE_MIDDLEWARE_SECONDS = 3600
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

MIDDLEWARE_CLASSES += (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


# Configura tu valor DSN
RAVEN_CONFIG = {
    'dsn': 'http://a3e0c9c9496243248d166cc5eceae130:2ebea0d205894fa28e044351b57dcef8@sentry.o2w.es/26',
}


INSTALLED_APPS = INSTALLED_APPS + (
    'raven.contrib.django.raven_compat',
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
