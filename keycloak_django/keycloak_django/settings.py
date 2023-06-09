"""
Django settings for keycloak_django project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
from .secrets import SECRET_KEY, DB_USER, DB_PASSWORD, OIDC_DEV_ADMIN_USERNAME, OIDC_DEV_ADMIN_PASSWORD, \
    EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_HOST, OIDC_RP_CLIENT_SECRET, OIDC_RP_REALM_NAME, OIDC_RP_CLIENT_ID, \
    DB_HOST, DB_PORT

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY

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
    'keycloak_auth',
    'mozilla_django_oidc',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'mozilla_django_oidc.middleware.SessionRefresh',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'keycloak_auth.middleware.JwtMiddleware'
]

ROOT_URLCONF = 'keycloak_django.urls'

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

WSGI_APPLICATION = 'keycloak_django.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_keycloak_user',
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'keycloak_auth/static')]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = (
    'keycloak_auth.auth.KeycloakOIDCAuthenticationBackend',
    # 'mozilla_django_oidc.auth.OIDCAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)


OIDC_RP_CLIENT_SECRET = OIDC_RP_CLIENT_SECRET  # Keycloak Secret
OIDC_RP_SIGN_ALGO = 'RS256'
OIDC_DEV_ADMIN_USERNAME = OIDC_DEV_ADMIN_USERNAME
OIDC_DEV_ADMIN_PASSWORD = OIDC_DEV_ADMIN_PASSWORD

OIDC_OP_BASE_URL = "http://127.0.0.1:28080/auth/"
OIDC_OP_AUTHORIZATION_ENDPOINT = 'http://127.0.0.1:28080/auth/realms/dev/protocol/openid-connect/auth'
OIDC_OP_TOKEN_ENDPOINT = 'http://127.0.0.1:28080/auth/realms/dev/protocol/openid-connect/token'
OIDC_OP_USER_ENDPOINT = 'http://127.0.0.1:28080/auth/realms/dev/protocol/openid-connect/userinfo'
OIDC_OP_JWKS_ENDPOINT = 'http://127.0.0.1:28080/auth/realms/dev/protocol/openid-connect/certs'
OIDC_OP_LOGOUT_ENDPOINT = "http://127.0.0.1:28080/auth/realms/dev/protocol/openid-connect/logout"

OIDC_RP_REALM_NAME = OIDC_RP_REALM_NAME
OIDC_RP_CLIENT_ID = OIDC_RP_CLIENT_ID  # Keycloak Client ID

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
REDIRECT_URI = 'http://127.0.0.1:8000/callback/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = EMAIL_HOST
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD

AUTH_USER_MODEL = 'keycloak_auth.CustomUser'


