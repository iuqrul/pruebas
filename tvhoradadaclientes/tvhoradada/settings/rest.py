
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'clientes.auth.ClienteBackend',
)


REST_FRAMEWORK = {
     'DEFAULT_PERMISSION_CLASSES': (
         'rest_framework.permissions.IsAuthenticated',
     ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
}
