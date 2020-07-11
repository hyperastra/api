"""
Django settings for Playbook API project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import json
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import firebase_admin
from firebase_admin import credentials

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "r@n$2iaheddouqi%rfzp0l7z*0@s2^m#5+ggk%-3u5k0h&gsb9"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# CORS allowed host
ALLOWED_HOSTS = ["*"]

# Application definition, in production better to remove the admin
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "core",
    "project",
    "store",
    "workspace"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.gzip.GZipMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

ASGI_APPLICATION = "config.routing.application"
WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"

DEFAULT_APPLICATION_URL = "http://localhost:4200"

CORS_ORIGIN_WHITELIST = [DEFAULT_APPLICATION_URL]
# Rest Framework settings
# https://www.django-rest-framework.org/api-guide/settings

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 40,
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
        "rest_framework.permissions.DjangoModelPermissions",
    ],
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    "DEFAULT_PARSER_CLASSES": ["rest_framework.parsers.JSONParser"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "core.authenticators.FirebaseAuthentication",
        'core.authenticators.ApiKeyAuthentication'
    ],
}

AUTH_USER_MODEL = 'core.User'
fb_service_key = os.getenv(
    "FIREBASE_CREDENTIALS",
    default='{"type":"service_account","project_id":"hyperastra-development","private_key_id":"a057db999b9858de16d374f41722c432abc92cf6","private_key":"-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZMH9EU5A4Duu1\njSKDVNzvwbnj6BS\/cJoR0toYmEf8e\/+coe6642ybJww6Rh8aE3v\/l9qyiXgGLGzS\nO9Rt4JqCXUQ9M2\/Btsf\/cx5zRu\/h1s\/8uoRJkb+I94n9bF9solyxW+JiekOO+ieq\nKyHU5iXDSj55ie9K\/GAVmq7J2+r3cXAjx8wk6M8aNAMnWn00OVz997hm5fDOc4OG\nxf2WTkg\/98H1oICOIbMTN9l2TQvvvhXjxmIR52JqPtviLL8UdAdQh0oiWMpAksVV\n2WYqK6y4JZOjJnRSh9Bm\/n2zusztbrCexcDJVJL3f+9cMm8INJgZTlDVRwZHRFoE\n5e7rRm37AgMBAAECggEAIYC7KRGQ3izjDFL0n3iwSiXCpJbw2GUoxxYVAZVACYEh\nOYq7NkYNw1M\/LiAR\/SZDSvakTEUraBxjPvzutHJgszpq49vy4dltuYiLCnJHX7mQ\nxOYKsQSUHK8+sIKOp8XV8aAAaHt+v2f0RWo44kwMSDdEMuBlstYChmKhks7jTH8A\n344nZRaPOWVFJ8o4rgkneyikKsbgcjROWji1g08GgtYuSqjSdNiH\/ipFyYC3RJuZ\nu445AQtTgHrtpwrG8HqceQcg5YINt+C37gqdV3mGhB9JTKQSKCQFPUx4Y6WqNGgJ\nMmnGvXHGBIVEzdW7Ssrv\/MIlUS4FdRmygM6hilD\/9QKBgQD2+Kv2ouv3Qow6\/kWT\nx1gL94IpcEHVoOz8X8geL0AiCwG93M46fUjr+EWU0PgJRfsF6FVhBmlXpVIT8j+R\niwrebfSvtcUKAORlHuROK220W0NRBBueD2IP0qF1NPi9pS90qJZ3KkLCE+Q5h\/xZ\ntBD\/0Wo3DtyDybtGgVZ6hOcgpQKBgQDhIRsGYxuW9D6w+duh8gf73qLaP\/y3pRSP\nxiS2Nvdp\/JM6lTQkn3bykRUwe2KJ3ZaWTXZ8JP8i1+f0I4X2hETcXnLmrhaZslgR\nd5RwnBNSE9UyGZuJPOajcAuabU8v26t1\/W19LD5PFw6HJNZ\/35Xegie8WfAIbopd\ndMS8z8ByHwKBgC0W12Zu9j+tQabfl1pUkamVpYjlOs\/C0qF85y9DlyTf95BvSKN7\nDh4utJ1nzXD7+sloUnYlUoQy5ZpIpvxucyyKzJpryC58XTZs\/mebHCtKYi7fXh9s\nVY3n+ZxJcIRHLTPSN65H4+pE8Wzje9nwuw3JcOfeaboR0YQcxuoVa5EVAoGAAmo3\nfv8LKbhe\/8j+WSNegI4n0w2CqXmk2dH3TNkUGFf0QFmfYJExVnLF9mosaWwuFFiq\nX7SJ5BbKzyyeYEGU94Qv2VeeuHFYTn+o4PhboLLDw7DQoU088B3gkfyAL\/Q8R5y7\nUu9pj7Ggn0R+5IpCckuVH4kbcQu2gkAhaCEWYGMCgYEAuUO+Bn7E3SSJasSwKO3S\nTUYdPqnyrhsc2QvXMZySdC3upckB8tIeSRI6g\/hVYAtSTF99O3NcgXuprzHsw12f\n5oYJUwhmlx+3FhSKDooAKIxcJ5PMWf3GTi1D1akXTPLFo\/FEm4vNXzg3FjZhtSvI\nbon3WQ1YcTshVv7aTNPw2+4=\n-----END PRIVATE KEY-----\n","client_email":"firebase-adminsdk-k43g5@hyperastra-development.iam.gserviceaccount.com","client_id":"108440787756025309328","auth_uri":"https:\/\/accounts.google.com\/o\/oauth2\/auth","token_uri":"https:\/\/oauth2.googleapis.com\/token","auth_provider_x509_cert_url":"https:\/\/www.googleapis.com\/oauth2\/v1\/certs","client_x509_cert_url":"https:\/\/www.googleapis.com\/robot\/v1\/metadata\/x509\/firebase-adminsdk-k43g5%40hyperastra-development.iam.gserviceaccount.com"}',
)
fb_service_key = fb_service_key.replace("\n", "\\n")
fb_credentials = json.loads(fb_service_key)
cred = credentials.Certificate(fb_credentials)
firebase_admin.initialize_app(cred)

# TODO: Add rq-worker later
# TODO: Add Twilio API key
# TODO: Add Sendgrid API key
# TODO: Add Stripe API key
# TODO: Add currency converter API key
