from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Movie, Genre
from .serializers import MovieSerializer, GenreSerializer


class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()
        genre_id = self.request.query_params.get("genre_id")
        if genre_id != None:
            queryset = Movie.objects.filter(genre_id=genre_id)
        return queryset


class GenreViewSet(ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
