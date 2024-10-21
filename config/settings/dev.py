from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(weeks=480),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(weeks=480),
    'ROTATE_REFRESH_TOKENS': True,
}
REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"].append('rest_framework.authentication.BasicAuthentication')
THUMBNAIL_WIDTH = 300

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}
