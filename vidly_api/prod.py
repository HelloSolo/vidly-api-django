from settings import *

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "railway",
        "HOST": "containers-us-west-161.railway.app",
        "USER": "postgres",
        "PASSWORD": "n9X0UF4EjASv4m2EU4E5",
        "PORT": "7195",
    }
}
