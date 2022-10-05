from django.urls import path, include
from .views import (
    CustomerViewSet,
    GenreViewSet,
    MoviePosterViewSet,
    MovieViewSet,
    WatchListViewSet,
)
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter


router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")
router.register("genres", GenreViewSet)
router.register("customers", CustomerViewSet, basename="customer")

movie_router = NestedDefaultRouter(router, "movies", lookup="movie")
movie_router.register("images", MoviePosterViewSet, basename="movie-images")

customer_router = NestedDefaultRouter(router, "customers", lookup="customer")
customer_router.register("watchlists", WatchListViewSet, basename="customer-watchlist")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(movie_router.urls)),
    path("", include(customer_router.urls)),
]
