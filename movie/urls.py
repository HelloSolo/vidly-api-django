from django.urls import path
from .views import genre_detail, MovieList, MovieDetail

urlpatterns = [
    path("movie/", MovieList.as_view()),
    path("movie/<int:pk>/", MovieDetail.as_view()),
    path("genre/<int:pk>/", genre_detail, name="genre-detail"),
]
