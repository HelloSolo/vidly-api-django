from .common import *


DEBUG = True

ALLOWED_HOSTS = ["*"]

SECRET_KEY = "django-insecure-ma^cg$qf9ly-^4&eomakqqu*b6)%y3^^mw(**ct*hfbisctld4"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "vidly",
        "HOST": "127.0.0.1",
        "USER": "root",
        "PASSWORD": "Underw@ter",
    }
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
