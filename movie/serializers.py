from os import set_inheritable
from rest_framework import serializers
from .models import Genre, Movie


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    genre = GenreSerializer()
    numberInStock = serializers.IntegerField()
    dailyRentalRate = serializers.DecimalField(max_digits=3, decimal_places=2)
