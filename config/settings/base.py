# common settings for the server
import os

from django.core.exceptions import ImproperlyConfigured
from unipath import Path


BASE_DIR = Path(__file__).ancestor(3)

SECRET_KEY = os.environ['COVID_SECRET_KEY'] if 'COVID_SECRET_KEY' in os.environ else None

DEBUG = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'rest_framework',
    'bootstrap4',
    'account',
    'pinax_theme_bootstrap',
    'bootstrapform',
    'sampledatahelper',

    'fuckcovid.auth',
    'fuckcovid.hospitals',
    'fuckcovid.makers',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'account.middleware.LocaleMiddleware',
    'account.middleware.TimezoneMiddleware',
]

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.child('fuckcovid').child('templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'account.context_processors.account',
                'pinax_theme_bootstrap.context_processors.theme',
            ],
        },
    },
]

AUTH_USER_MODEL = 'fuckcovid_auth.User'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

BOOTSTRAP4 = {
    "css_url": "https://stackpath.bootstrapcdn.com/bootswatch/4.4.1/minty/bootstrap.min.css",
}

#django-user-accounts settings

# Sample data generation

SAMPLEDATAHELPER_MODELS = [
    { 'model': 'sites.Site', 'number': 1, 'fields_overwrite': [('domain', '127.0.0.1'), ('name', '127.0.0.1')]},
    { 'model': 'fuckcovid_auth.User', 'number': 10, },
    { 'model': 'hospitals.Region', 'number': 10, },
    { 'model': 'hospitals.Hospital', 'number': 100, },
    { 'model': 'hospitals.Resource', 'number': 1000, },
    { 'model': 'hospitals.Need', 'number': 250, 'fields_overwrite': [('amount_per_day', lambda _, sd: sd.int(10, 1500))], },
    { 'model': 'makers.Maker', 'number': 30, },
    { 'model': 'makers.Production', 'number': 200, 'fields_overwrite': [('amount_per_day', lambda _, sd: sd.int(10, 1500))]},
]
