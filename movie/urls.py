from django.urls import path
from .views import movie_detail, movie_list

urlpatterns = [
    path("movies/", movie_list),
    path("movies/<int:id>/", movie_detail),
]
