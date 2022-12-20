from .common import *


DEBUG = False

SECRET_KEY = "django-insecure-ma^cg$qf9ly-^4&eomakqqu*b6)%y3^^mw(**ct*hfbisctld4"

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": "vidly",
#         "HOST": "127.0.0.1",
#         "USER": "root",
#         "PASSWORD": "Underw@ter",
#     }
# }

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "railway",
        "HOST": "containers-us-west-174.railway.app",
        "USER": "root",
        "PASSWORD": "5gc1oLbcZLuprqt50eDS",
        "PORT": "6380",
    }
}
