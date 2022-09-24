from rest_framework import serializers
from .models import Genre, Movie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()

    class Meta:
        model = Movie
        fields = ["id", "title", "genre", "numberInStock", "dailyRentalRate"]


class AddMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["title", "genre", "numberInStock", "dailyRentalRate"]
