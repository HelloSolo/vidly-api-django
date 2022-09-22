from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode
from .models import Movie, Genre

# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    actions = ["clear_stock"]
    autocomplete_fields = ["genre"]
    list_display = ["title", "genre", "numberInStock", "dailyRentalRate"]
    list_editable = ["numberInStock", "dailyRentalRate"]
    list_filter = ["genre"]
    list_per_page = 10
    list_select_related = ["genre"]
    ordering = ["title"]
    search_fields = ["title"]

    @admin.action(description="Clear Stock")
    def clear_stock(self, request, queryset):
        update_count = queryset.update(numberInStock=0)
        self.message_user(request, f"{update_count} movies has been updated")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name", "movie_count"]
    search_fields = ["name"]

    @admin.display(ordering="movie_count")
    def movie_count(self, genre):
        url = f'{reverse("admin:movie_movie_changelist")}?{urlencode({"genre__id": genre.id})}'
        return format_html("<a href={}>{}</a>", url, genre.movie_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(movie_count=Count("movie"))
