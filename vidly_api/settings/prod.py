from .common import *
import dj_database_url

DEBUG = False

SECRET_KEY = os.getenv("SECRET_KEY")

DATABASES = {"default": dj_database_url.config()}

ALLOWED_HOSTS = ["web-production-43a4.up.railway.app"]
