import dj_database_url

from henrikac.settings import *

DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '.herokuapp.com',
    '.henrikac.com',
]

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

INSTALLED_APPS += (
    'gunicorn',
)

SECRET_KEY = get_env_variable('SECRET_KEY')

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

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
             'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
