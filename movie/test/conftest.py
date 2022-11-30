from rest_framework.test import APIClient
from core.models import User
from movie.models import SubcriptionType
from model_bakery import baker
import pytest


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def authenticate(api_client):
    SubcriptionType.objects.all().delete()
    User.objects.all().delete()
    client = api_client
    baker.make(SubcriptionType, plan="Free")
    user = baker.make(User)
    client.force_authenticate(user=user)
    return client
