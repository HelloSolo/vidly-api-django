import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vidly_api.settings.dev")

celery = Celery("vidly_api")
celery.config_from_object("django.conf:settings", namespace="CELERY")
celery.autodiscover_tasks()
