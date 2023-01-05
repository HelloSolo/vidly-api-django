from .common import *
import dj_database_url

DEBUG = False

SECRET_KEY = os.getenv("SECRET_KEY")

DATABASES = {"default": dj_database_url.config()}

ALLOWED_HOSTS = ["web-production-6a07.up.railway.app"]

RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
