"""
Django settings for pyclist project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

from os import path, environ

from django.utils.translation import gettext_lazy as _

from pyclist import conf


# Build paths inside the project like this: path.join(BASE_DIR, ...)
BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))

ADMINS = (
    ('Aleksey Ropan', 'aropan@clist.by'),
)

MANAGERS = ADMINS

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = 'noreply@clist.by'
EMAIL_HOST_PASSWORD = conf.EMAIL_HOST_PASSWORD
EMAIL_PORT = 587
EMAIL_USE_TLS = True

SERVER_EMAIL = 'Clist <%s>' % EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = 'Clist <%s>' % EMAIL_HOST_USER

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['clist.by', 'dev.clist.by', 'localhost']

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = conf.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = 'DJANGO_RUNSERVER_DEBUG' in environ

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'clist',
    'ranking',
    'tastypie',
    'my_oauth',
    'true_coders',
    'jsonify',  # https://pypi.python.org/pypi/django-jsonify/0.2.1
    'tastypie_swagger',
    'blog',
    'django_markdown',
    'tg',
    'notification',
    'crispy_forms',
    'events',
    'django_countries',
    'el_pagination',
    'easy_select2',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'pyclist.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': [
                'pyclist.templatetags.staticfiles'
            ]
        },
    },
]

WSGI_APPLICATION = 'pyclist.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


DATABASES_ = {
    'postgresql': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': conf.DB_NAME,
        'USER': conf.DB_USER,
        'PASSWORD': conf.DB_PASSWORD,
        'HOST': conf.DB_HOST,
        'PORT': conf.DB_PORT,
    },
}

DATABASES = {
    'default': DATABASES_['postgresql'],
}
DATABASES.update(DATABASES_)


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', _('English')),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = path.join(BASE_DIR, "static/")
STATIC_JSON_TIMEZONES = path.join(STATIC_ROOT, 'json', 'timezones.json')

STATICFILES_DIRS = [
    # path.join(BASE_DIR, "static/external/x-editable/dist/bootstrap3-editable"),
    # path.join(BASE_DIR, "static/external/font-awesome-4.3.0"),
    # path.join(BASE_DIR, "static/external/bootstrap-3.3.4-dist"),
    # path.join(BASE_DIR, "static/external/select2/dist"),
    # path.join(BASE_DIR, "static/external/select2-bootstrap-css/dist"),
    # path.join(BASE_DIR, "static/external/BootstrapXL/dist"),
    # path.join(BASE_DIR, "static/external/fullcalendar-2.3.2/dist"),
    # path.join(BASE_DIR, "static/external/awesome-bootstrap-checkbox/dist"),
    # path.join(BASE_DIR, "static/external/bootboxjs"),
]

if DEBUG:
    STATICFILES_DIRS.append(STATIC_ROOT)
    STATIC_ROOT = None
# else:
    # STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

TASTYPIE_DEFAULT_FORMATS = ['json', 'jsonp', 'yaml', 'xml', 'plist']

LOGIN_URL = '/login/'

APPEND_SLASH = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'development': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': path.join(BASE_DIR, 'logs', 'dev.log'),
            'formatter': 'verbose',
        },
        'production': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7,
            'filename': path.join(BASE_DIR, 'logs', 'prod.log'),
            'formatter': 'simple',
        },
        'telegrambot': {
            'level': 'DEBUG',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7,
            'filename': path.join(BASE_DIR, 'logs', 'telegram.log'),
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
        'django': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
        },
        'telegrambot': {
            'handlers': ['telegrambot'],
            'level': 'DEBUG',
        },
        '': {
            'handlers': ['console', 'development', 'production'],
            'level': 'DEBUG',
        },
    },
}


DATA_UPLOAD_MAX_NUMBER_FIELDS = 100000


TELEGRAM_TOKEN = conf.TELEGRAM_TOKEN
TELEGRAM_NAME = '@ClistBot'
TELEGRAM_ADMIN_CHAT_ID = conf.TELEGRAM_ADMIN_CHAT_ID

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# CONSTANTS
VIEWMODE_ = 'list'
OPEN_NEW_TAB_ = False
ADD_TO_CALENDAR_ = 'enable'
COUNT_PAST_ = 3
GROUP_LIST_ = True
DEFAULT_TIME_ZONE_ = 'UTC'
HOST_ = 'localhost:8000' if DEBUG else 'clist.by'
HTTP_HOST_ = 'http://' + HOST_
HTTPS_HOST_ = 'https://' + HOST_
EMAIL_PREFIX_SUBJECT_ = '[Clist] '
TIME_FORMAT_ = '%d.%m %a %H:%M'
LIMIT_N_TOKENS_VIEW = 3
LIMIT_TOKENS_VIEW_WAIT_IN_HOURS = 24
