from model_bakery import baker
from rest_framework import status
import pytest
from movie.models import Movie, Genre


@pytest.mark.django_db
def test_get_movies(api_client):
    baker.make(Movie, _quantity=5)
    response = api_client.get("/api/movies/")

    assert response.status_code == status.HTTP_200_OK
