from .common import *
import dj_database_url

DEBUG = os.getenv("DEBUG")

SECRET_KEY = os.getenv("SECRET_KEY")

# DATABASES = {
#     "default": {
#         "ENGINE": os.getenv("ENGINE"),
#         "NAME": os.getenv("NAME"),
#         "HOST": os.getenv("HOST"),
#         "USER": os.getenv("USER"),
#         "PASSWORD": os.getenv("PASSWORD"),
#         "PORT": os.getenv("PORT"),
#     }
# }

DATABASES = {"default": dj_database_url.config()}
