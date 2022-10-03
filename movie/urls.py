from django.urls import path, include
from .views import GenreViewSet, MoviePosterViewSet, MovieViewSet
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter


router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")
router.register("genres", GenreViewSet)
# router.register("customers")

movie_router = NestedDefaultRouter(router, "movies", lookup="movie")
movie_router.register("images", MoviePosterViewSet, basename="movie-images")
# movie_router.register("promotion", PromotionViewSet, basename="movie-promotion")

urlpatterns = [path("", include(router.urls)), path("", include(movie_router.urls))]
