from .base import *

DEFAULT_APPLICATION_URL = "http://localhost:4200"

CORS_ORIGIN_WHITELIST = [DEFAULT_APPLICATION_URL]

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "database-name",
        "USER": "database-username",
        "PASSWORD": "database-username-password",
        "HOST": "database-host",
        "PORT": 5432,
    }
}
