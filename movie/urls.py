from django.urls import path, include
from .views import (
    CustomerViewSet,
    GenreViewSet,
    MoviePosterViewSet,
    MovieViewSet,
    SubscriptionTypeViewSet,
    WatchListViewSet,
)
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter


router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")
router.register("genres", GenreViewSet)
router.register("subscriptions", SubscriptionTypeViewSet)
router.register("customers", CustomerViewSet, basename="customer")
router.register("watchlists", WatchListViewSet, basename="watchlist")

movie_router = NestedDefaultRouter(router, "movies", lookup="movie")
movie_router.register("images", MoviePosterViewSet, basename="movie-images")

urlpatterns = [path("", include(router.urls)), path("", include(movie_router.urls))]
