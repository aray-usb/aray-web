"""
Django settings for aray project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import datetime
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '6-gut-+)a99y$&jkuvq7j940b)q0-gx$9j(x1%4k=s11jjz$59')

# Para la recepción de errores
ADMINS = (
    ('Aray', 'arayusb@gmail.com'),
)

# IMPORTANTE: Esta variable permite saber si estamos en un entorno de desarrollo
# o en produción
# SECURITY WARNING: don't run with debug turned on in production!
CUR_DOMAIN = os.environ.get('CUR_DOMAIN', 'localhost')
DEBUG = CUR_DOMAIN == 'localhost'

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'aray-usb.herokuapp.com',
    'arayusb.com.ve',
    'aray.com.ve',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.api',
    'apps.accounts',
    'apps.dashboard',
    'apps.dashboard.resources_management',
    'apps.dashboard.personal_management',
    'apps.dashboard.map',
    'apps.dashboard.assignments',
    'rest_framework',
    'rest_framework.authtoken',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'aray.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'aray.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES_LIST = {
    'aray-usb': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', ''),
        'USER': os.environ.get('DB_USER', ''),
        'PASSWORD': os.environ.get('DB_PASS', ''),
        'HOST': os.environ.get('DB_HOST', ''),
        'PORT': '5432',
        'OPTIONS': {
            'connect_timeout': None,
        }
    },
    'localhost': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES = {'default': DATABASES_LIST[CUR_DOMAIN]}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Caracas'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Important for Heroku
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

# Configuraciones de autenticación
PASSWORD_RESET_TIMEOUT_DAYS = 3
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'dashboard:index'

# Se cierra la sesion en dos dias: 60 segundos por minuto,
# 60 minutos por hora, 24 horas por día, 2 días
SESSION_COOKIE_AGE = 60 * 60 * 24 * 2

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# API

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
}

# Deshabilita la API Web si no es desarrollo local
if not DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
        'rest_framework.renderers.JSONRenderer',
    )

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=14),
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}

AUTHENTICATION_BACKENDS = (
    ('django.contrib.auth.backends.ModelBackend'),
)

# Email Config
EMAIL_USE_TLS = True
EMAIL_HOST = os.environ.get('ARAY_EMAIL_HOST', "")
EMAIL_HOST_USER = os.environ.get('ARAY_EMAIL_USER', "")
EMAIL_HOST_PASSWORD = os.environ.get('ARAY_EMAIL_PASSWORD', "")
EMAIL_PORT = 587

# Log de errores para Heroku
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
        },
    },
}