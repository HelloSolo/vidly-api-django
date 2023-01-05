from model_bakery import baker
from rest_framework import status
import pytest
from movie.models import Genre


@pytest.mark.django_db
def test_get_movies(api_client):
    baker.make(Genre, _quantity=10)
    response = api_client.get("/api/genres/")

    assert response.status_code == status.HTTP_200_OK
