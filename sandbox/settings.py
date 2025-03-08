"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""


import sys
import environ
from datetime import timedelta
from pathlib import Path


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR / "src"))
sys.path.append(str(BASE_DIR)) # -> ecommerce directory

# Take environment variables from .env file
environ.Env.read_env(BASE_DIR / ".env")
from core.languages import LANGUAGES as CORE_LANGUAGES


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3&a@-m_y)^t7nm6w(bcbb!5ne6+4!__r%-1bj&5g)96$l+8qy*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps
    'account',
    'catalogue',
    'core',
    'products',

    # third-party apps
    'rest_framework',
    'rest_framework_simplejwt',
    'django_filters',
    'treebeard',
    'debug_toolbar',
    'drf_spectacular',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'sandbox' / 'templates',
            BASE_DIR / 'src' / 'templates',
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": env("DATABASE_ENGINE", default="django.db.backends.sqlite3"),
        "NAME": env("DATABASE_NAME", default="db.sqlite3"),
        "USER": env("DATABASE_USER", default=None),
        "PASSWORD": env("DATABASE_PASSWORD", default=None),
        "HOST": env("DATABASE_HOST", default=None),
        "PORT": env("DATABASE_PORT", default=None),
    }
}


# Caches

CACHES = {
    "default": {
        "BACKEND": env("CACHE_BACKEND", default="django.core.cache.backends.locmem.LocMemCache"),
        "LOCATION": env("CACHE_LOCATION", default=None),
        "TIMEOUT": env("CACHE_TIMEOUT", default=300),
    }
}

# User model

AUTH_USER_MODEL = 'account.User'


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]


# LOGGING
import logging

# Ensure logs directory exists
LOGS_DIR = BASE_DIR / "logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)  # Creates 'logs/' if it doesn't exist
class MultiLineFormatter(logging.Formatter): # TODO Bad practice
    def format(self, record):
        original_message = super().format(record)
        max_length = 140
        lines = [original_message[i:i + max_length] for i in range(0, len(original_message), max_length)]
        s = '\n'.join(lines)
        return "%s \n" % s

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'multiline': {
            '()': MultiLineFormatter,
            'format': '[%(levelname)s]: %(message)s',
        },
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },

        'logfile': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / 'logs' / 'debug.log',
            'formatter': 'multiline',
            'mode': 'a',
            'maxBytes': 7000,
            'backupCount': 2,
            'delay': False
        }
    },
}

if env("LOGGING_QUERIES", default=False):
    LOGGING.setdefault(
        'loggers', {
            'django.db.backends': {
                'level': 'DEBUG',
                'handlers': ['logfile'],
                'propagate': False,
            }
        }
    )


REST_FRAMEWORK = {
    # YOUR SETTINGS
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=4),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
}
