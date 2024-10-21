from .base import *


DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pyler_table',
        'USER': 'pyler',
        'PASSWORD': 'pyler1234',
        'HOST': '127.0.0.1',
        'PORT': '3300',
        'OPTIONS': {
            'charset': 'utf8mb4',
        }
    },
    # 'read': {...},
    # 'write': {...},
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(weeks=12),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(weeks=12),
    'ROTATE_REFRESH_TOKENS': True,
}

THUMBNAIL_WIDTH = 400
