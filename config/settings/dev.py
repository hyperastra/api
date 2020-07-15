from .base import *

DEFAULT_APPLICATION_URL = "http://localhost:4200"

CORS_ORIGIN_WHITELIST = [DEFAULT_APPLICATION_URL]
GDAL_LIBRARY_PATH = r"C:\Program Files (x86)\GDAL\gdal300"
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "hyperastra",
        "USER": "postgres",
        "PASSWORD": "test",
        "HOST": "localhost",
        "PORT": 5432,
    }
}
