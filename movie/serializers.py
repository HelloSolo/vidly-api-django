from rest_framework import serializers
from .models import Customer, Genre, Movie, MoviePoster


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["_id", "name"]


class MoviePosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviePoster
        fields = ["id", "image"]

    def create(self, validated_data):
        movie_id = self.context["movie_id"]
        return MoviePoster.objects.create(movie_id=movie_id, **validated_data)


class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    images = MoviePosterSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = [
            "_id",
            "title",
            "genre",
            "imdbRating",
            "description",
            "releaseDate",
            "images",
            "promoted",
        ]


class AddMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["title", "genre", "imdbRating", "description", "releaseDate"]


# class PromotionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Promotion
#         fields = ["movie_id", "images"]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["user_id", "watchList", "subscriptionType", "subscriptionStatus"]
