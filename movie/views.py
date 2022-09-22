from itertools import product
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer

# Create your views here.
@api_view()
def movie_list(request):
    queryset = Movie.objects.select_related("genre").all()
    serializer = MovieSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def movie_detail(request, pk):
    movie = Movie.objects.get(pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view()
def genre_detail(request, pk):
    return Response("ok")
