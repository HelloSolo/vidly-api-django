from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Movie, Genre
from .serializers import MovieSerializer, GenreSerializer
from .paginate import DefaultPagination
from .filter import MovieFilter


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.select_related("genre").all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MovieFilter
    ordering_fields = ["dailyRentalRate", "numberInStock"]
    pagination_class = DefaultPagination
    search_fields = ["title"]


class GenreViewSet(ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
