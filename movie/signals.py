from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer, SubcriptionType


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_customer_for_new_user(sender, **kwargs):
    if kwargs["created"]:
        subcription = SubcriptionType.objects.get(plan="Free")
        Customer.objects.create(user=kwargs["instance"], subscription_id=subcription.id)
