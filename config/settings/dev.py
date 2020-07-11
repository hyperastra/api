from .base import *
DEFAULT_APPLICATION_URL = "http://localhost:4200"

CORS_ORIGIN_WHITELIST = [
    DEFAULT_APPLICATION_URL
]

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'hyperastra',
        'USER': 'postgres',
        'PASSWORD': 'ada280991',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
