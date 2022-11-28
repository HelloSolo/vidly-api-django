from core.models import User
from django.db import transaction
from ..models import SubcriptionType, Movie, Genre
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
import pytest


@pytest.fixture
def database_setup():
    @transaction.atomic
    def queries(username, plan):
        SubcriptionType.objects.create(
            plan=plan, monthly_price=1, resolution=" ", video_quality=" ", devices=""
        )
        user = User.objects.create(username=username, password="loophole")
        genre = Genre.objects.create(name=" ")
        movie = Movie.objects.create(title=" ", genre_id=genre._id, imdbRating=7.8)

        return user, movie

    return queries


@pytest.mark.django_db
class TestCreateWatchlist:
    # @pytest.mark.skip
    def test_if_user_is_anonymous_returns_401(self):
        client = APIClient()
        response = client.post("/api/watchlists/", {"movie": 1})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    # @pytest.mark.skip
    def test_if_data_is_invalid_returns_400(self, database_setup):
        (user, _) = database_setup("b", "d")

        client = APIClient()
        client.force_authenticate(user=user)
        response = client.post("/api/watchlists/", {"movie": ""})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["movie"] is not None

    @pytest.mark.skip
    def test_if_user_is_authenticated_returns_201(self, database_setup):
        (user, movie) = database_setup("a", "c")

        client = APIClient()
        client.force_authenticate(user=user)
        response = client.post("/api/watchlists/", {"movie": movie._id})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["movie"] > 0


# =============================================================Django Test==============================================================
# class CreateWatchlistTest(APITestCase, APIClient):
#     def test_if_user_is_anonymous_returns_401(self):
#         response = self.client.post("/api/watchlists/", {"movie": 1})

#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

#     def test_if_user_is_authenticated_returns_201(self):
#         SubcriptionType.objects.create(
#             plan=" ", monthly_price=1, resolution=" ", video_quality=" ", devices=""
#         )
#         genre = Genre.objects.create(name=" ")
#         movie = Movie.objects.create(title=" ", genre_id=genre._id, imdbRating=7.8)
#         user = User.objects.create(username="user1@domain.com", password="loophole")

#         self.client.force_authenticate(user=user)
#         response = self.client.post("/api/watchlists/", {"movie": movie._id})

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_if_data_is_invalid_returns_400(self):
#         SubcriptionType.objects.create(
#             plan=" ", monthly_price=1, resolution=" ", video_quality=" ", devices=""
#         )
#         user = User.objects.create(username="user2@domain.com", password="loophole")

#         client = APIClient()
#         client.force_authenticate(user=user)
#         response = client.post("/api/watchlists/", {"movie_id": ""})

#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
