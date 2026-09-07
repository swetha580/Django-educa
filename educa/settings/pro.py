from .base import *

DEBUG = False

ADMINS = (
    ('swetha', 'swetha@testpress.in'),
)

ALLOWED_HOSTS = ['.educaproject.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': 'R8#vT2!mQ7@kL5$zP9x',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True