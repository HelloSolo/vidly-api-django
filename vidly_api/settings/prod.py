from .common import *
import dj_database_url

DEBUG = False

SECRET_KEY = os.getenv("SECRET_KEY")

DATABASES = {"default": dj_database_url.config()}

ALLOWED_HOSTS = [os.getenv("HOSTNAME")]

MEDIA_URL = "/vidly/media/"

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.RawMediaCloudinaryStorage"

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": "vidly-storage",
    "API_KEY": "912221361294972",
    "API_SECRET": os.getenv("CLOUD_API_SECRET"),
}
