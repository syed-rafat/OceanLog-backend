"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
import cloudinary
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+d!k-*79!f_(a#w(7!u(z-%8d48p&#b48f5r+rv^d6c1p^o_#8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['oclogbackend.azurewebsites.net', '127.0.0.1', 'localhost', '127.0.0.1:8000']

# if 'CODESPACE_NAME' in os.environ:
#     CSRF_TRUSTED_ORIGINS = [f'https://{os.getenv("CODESPACE_NAME")}-8000.{os.getenv("GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN")}']

CSRF_TRUSTED_ORIGINS=['https://oclogbackend.azurewebsites.net']

# for printing in backend console. restpassword reset
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd_party
    'rest_framework',
    "corsheaders",
    'cloudinary',
    # 'django_rest_passwordreset',

    # local
    'core',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    # "django.middleware.common.CommonMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

hostname = os.environ['DBHOST']
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ['DBNAME'],
#         'HOST': hostname + ".postgres.database.azure.com",
#         'USER': os.environ['DBUSER'],
#         'PASSWORD': os.environ['DBPASS'] 
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': postgres,
        'HOST': hostname + ".postgres.database.azure.com",
        'USER': os.environ['DBUSER'],
        'PASSWORD': os.environ['DBPASS'] 
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




# needed for cookie
# CORS_ALLOW_CREDENTIALS = True

# from corsheaders.defaults import default_headers

# CORS_ALLOW_HEADERS = list(default_headers) + [
#     "my-custom-header",
# ]


cloudinary.config(
    cloud_name="dylqfbsq2",
    api_key="788139839676776",
    api_secret="O2zmvQ_J-KkpUsM0TXnuGA0W-lc"
)

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'core.authenticate.JWTAuth',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_METADATA_CLASS': 'rest_framework.metadata.SimpleMetadata',
}

# email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_password'



# print(os.environ.get('CLOUDINARY_CLOUD_NAME'))

# DJOSER = {
#     "PASSWORD_RESET_CONFIRM_URL": "reset_password/{uid}/{token}",
#     'USERNAME_RESET_CONFIRM_URL': '/username/reset/confirm/{uid}/{token}',
#     'ACTIVATION_URL': '#/activate/{uid}/{token}',
#     'SEND_ACTIVATION_EMAIL': True,
#     'SERIALIZERS': {},
# }


# SIMPLE_JWT = {
#   'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
#   'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
#   'ROTATE_REFRESH_TOKENS': False,
#   'BLACKLIST_AFTER_ROTATION': True,
#   'UPDATE_LAST_LOGIN': False,

#   'ALGORITHM': 'HS256',
#   'SIGNING_KEY': SECRET_KEY,
#   'VERIFYING_KEY': None,
#   'AUDIENCE': None,
#   'ISSUER': None,

#   'AUTH_HEADER_TYPES': ('Bearer',),
#   'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
#   'USER_ID_FIELD': 'id',
#   'USER_ID_CLAIM': 'user_id',
#   'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

#   'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
#   'TOKEN_TYPE_CLAIM': 'token_type',

#   'JTI_CLAIM': 'jti',

#   'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
#   'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
#   'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),

#   # custom
#     'AUTH_COOKIE': 'access_token',  # Cookie name. Enables cookies if value is set.
#   'AUTH_COOKIE_DOMAIN': None,     # A string like "example.com", or None for standard domain cookie.
#   'AUTH_COOKIE_SECURE': False,    # Whether the auth cookies should be secure (https:// only).
#   'AUTH_COOKIE_HTTP_ONLY' : True, # Http only cookie flag.It's not fetch by javascript.
#   'AUTH_COOKIE_PATH': '/',        # The path of the auth cookie.
#   'AUTH_COOKIE_SAMESITE': 'None',  # Whether to set the flag restricting cookie leaks on cross-site requests. This can be 'Lax', 'Strict', or None to disable the flag.
# }
