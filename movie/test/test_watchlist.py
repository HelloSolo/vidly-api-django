from core.models import User
from movie.models import Movie, WatchList, SubcriptionType
from model_bakery import baker
from rest_framework import status
import pytest


@pytest.fixture
def create_watchlist():
    def do_create_watchlist(movie, client):
        return client.post("/api/watchlists/", movie)

    return do_create_watchlist


@pytest.mark.django_db
class TestAddMovieToWatchlist:
    def test_if_user_is_anonymous_returns_401(self, api_client, create_watchlist):
        movie = baker.make(Movie)
        response = create_watchlist({"movie": movie._id}, api_client)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_data_is_invalid_returns_400(self, authenticate, create_watchlist):
        response = create_watchlist({"movie": "a"}, authenticate)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["movie"] is not None

    def test_if_user_is_authenticated_returns_201(self, authenticate, create_watchlist):
        movie = baker.make(Movie)

        response = create_watchlist({"movie": movie._id}, authenticate)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["movie"] > 0


@pytest.mark.django_db
class TestDeleteMovieFromWatch:
    def test_delete_movie_from_watchlist(self, api_client):
        baker.make(SubcriptionType, plan="Free")
        client = api_client
        user = baker.make(User)

        client.force_authenticate(user=user)
        watchlist = baker.make(WatchList, user=user)
        response = client.delete(f"/api/watchlists/{watchlist.id}/")

        assert response.status_code == status.HTTP_204_NO_CONTENT
