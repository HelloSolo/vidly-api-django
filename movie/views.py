from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Movie, Genre, MoviePoster, Promotion
from .serializers import (
    AddMovieSerializer,
    CustomerSerializer,
    MoviePosterSerializer,
    MovieSerializer,
    GenreSerializer,
    PromotionSerializer,
)
from .filter import MovieFilter
from .paginate import DefaultPagination


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.prefetch_related("images").select_related("genre").all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MovieFilter
    pagination_class = DefaultPagination
    ordering_fields = ["imbdRating", "releaseDate"]
    search_fields = ["title"]

    def get_serializer_class(self):
        if self.request.method == "POST" or self.request.method == "PUT":
            return AddMovieSerializer
        return MovieSerializer

    def paginate_queryset(self, queryset):
        if self.request.headers["Host"] == "localhost:8000":
            return None
        return super().paginate_queryset(queryset)


class MoviePosterViewSet(ModelViewSet):
    serializer_class = MoviePosterSerializer

    def get_queryset(self):
        return MoviePoster.objects.filter(movie_id=self.kwargs["movie_pk"])

    def get_serializer_context(self):
        return {"movie_id": self.kwargs["movie_pk"]}


class GenreViewSet(ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class PromotionViewSet(ModelViewSet):
    queryset = Promotion.objects.select_related("movie").all()
    serializer_class = PromotionSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Promotion.objects.select_related("user").all()
    serializer_class = CustomerSerializer
