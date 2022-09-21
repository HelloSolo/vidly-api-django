from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode
from .models import Movie, Genre

# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "genre", "numberInStock", "dailyRentalRate"]
    list_editable = ["numberInStock", "dailyRentalRate"]
    list_per_page = 10
    ordering = ["title"]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name", "movie_count"]

    @admin.display(ordering="movie_count")
    def movie_count(self, genre):
        url = f'{reverse("admin:movie_movie_changelist")}?{urlencode({"genre__id": genre.id})}'
        return format_html("<a href={}>{}</a>", url, genre.movie_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(movie_count=Count("movie"))
