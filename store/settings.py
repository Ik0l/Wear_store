# -*- coding:utf-8 -*-

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
path = lambda *args: os.path.join(BASE_DIR, *args).replace('\\', '/')

SECRET_KEY = '+dy&m(egj0s96l7(6-#4mz9hj)l#7reya(d9*f3z*wgem)d3k*'

DEBUG = True
TEMPLATE_DEBUG = DEBUG
COOKIE_DEBUG = DEBUG

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",

    "wear.context_processors.menu",
)

TEMPLATE_DIRS = {
    path('store', 'templates'),
}

ALLOWED_HOSTS = []


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'wear',
    'south',

    'debug_toolbar',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'store.urls'

WSGI_APPLICATION = 'store.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_ROOT = path('www', 'static', )
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    path('store', 'static'),
)

MEDIA_ROOT = path('www', 'media')
MEDIA_URL = '/media/'
LOCAL_MEDIA_ROOT = MEDIA_ROOT
LOCAL_MEDIA_URL = MEDIA_URL

FILE_UPLOAD_HANDLERS = (
    'wear.upload_handlers.MemoryFileUploadHandler',
    'wear.upload_handlers.TemporaryFileUploadHandler'
)
