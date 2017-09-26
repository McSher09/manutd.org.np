import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

INSTALLED_APPS = (
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',

    'froala_editor',
    'dj_pagination',
    'webstack_django_sorting',
    'auditlog',

    'versatileimagefield',

    'rest_framework',
    'rest_framework.authtoken',
    'solo',
    'fcm',
    'anymail',

    'apps.core',
    'apps.users',
    'apps.payment',
    'apps.page',
    'apps.dashboard',
    'apps.stats',
    'apps.events',
    'apps.post',
    'apps.partner',
    'apps.team',
    'apps.timeline',
    'apps.webhook',
    'apps.gallery',
    'apps.key',
    'apps.push_notification',
    'apps.contact',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'dj_pagination.middleware.PaginationMiddleware',
    'auditlog.middleware.AuditlogMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
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

ROOT_URLCONF = 'muscn.urls'
WSGI_APPLICATION = 'muscn.wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kathmandu'
USE_I18N = True
USE_L10N = True
USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 25,
    'DEFAULT_PERMISSION_CLASSES': [
        'apps.key.permissions.DistributedKeyAuthentication'

    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

from .user_settings import *  # noqa

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

ESEWA_SCD = 'manutd'

FCM_MAX_RECIPIENTS = 10000

ALIASES = [
    'Manchester United',
    'Man Utd',
    'Man United',
    'MUFC',
]

# TEMPLATE_DEBUG = False

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_NAME = 'sci'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_NAME = 'ct'
CSRF_COOKIE_SECURE = True

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/7",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

SOLO_CACHE = 'default'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        # 'opbeat': {
        #     'level': 'WARNING',
        #     'class': 'opbeat.contrib.django.handlers.OpbeatHandler',
        # },
    },
    'loggers': {
        'django': {
            # 'handlers': ['mail_admins', 'opbeat'],
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# E-mail settings
EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
DEFAULT_FROM_EMAIL = 'MUSC Nepal<info@manutd.org.np>'
SERVER_EMAIL = 'info@manutd.org.np'

try:
    from .local_settings import *  # noqa
except ImportError:
    pass

TEMPLATE_DEBUG = False
