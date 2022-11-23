import django_filters
from .models import Movie


class MovieFilter(django_filters.FilterSet):
    class Meta:
        model = Movie
        fields = {"genre_id": ["exact"], "imdbRating": ["gt", "lt"]}
