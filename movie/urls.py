from django.urls import path
from .views import genre_detail, movie_detail, movie_list

urlpatterns = [
    path("movie/", movie_list),
    path("movie/<int:pk>/", movie_detail),
    path("genre/<int:pk>/", genre_detail, name="genre-detail"),
]
