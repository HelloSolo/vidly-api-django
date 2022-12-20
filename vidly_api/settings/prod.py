from .common import *
import dj_database_url

DEBUG = os.getenv("DEBUG")

SECRET_KEY = os.getenv("SECRET_KEY")

DATABASES = {"default": dj_database_url.config()}
