from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_customer_for_new_user(sender, **kwargs):
    if kwargs["created"]:
        Customer.objects.create(user=kwargs["instance"])
