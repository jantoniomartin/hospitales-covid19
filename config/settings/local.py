# development settings

from .base import *

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child('db.sqlite3'),
    }
}

## django-user-accounts
ACCOUNT_EMAIL_CONFIRMATION_EMAIL = False
