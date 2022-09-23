from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Movie, Genre
from .serializers import MovieSerializer, GenreSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.select_related("genre").all()
    serializer_class = MovieSerializer


class GenreViewSet(ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
