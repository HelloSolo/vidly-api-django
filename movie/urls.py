from xml.etree.ElementInclude import include
from django.urls import path, include
from .views import GenreViewSet, MovieViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")
router.register("genres", GenreViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
