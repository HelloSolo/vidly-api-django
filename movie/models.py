from distutils.command.upload import upload
from email.mime import image
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

# Create your models here.


class Genre(models.Model):
    _id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]


class Movie(models.Model):
    _id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="movie")
    imdbRating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )
    description = models.CharField(max_length=1024, null=True)
    releaseDate = models.DateField(null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["title"]


class MoviePoster(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="movie/images")


class Customer(models.Model):
    SILVER = "SL"
    GOLD = "GD"
    BRONZE = "BR"

    SUBSCRIPTION_TYPE_CHOICES = [(SILVER, "silver"), (GOLD, "gold"), (BRONZE, "bronze")]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    watchList = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie")
    subscriptionStatus = models.BooleanField(default="false")
    subscriptionType = models.CharField(
        max_length=2,
        choices=SUBSCRIPTION_TYPE_CHOICES,
        default=BRONZE,
    )


class Promotions(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="promotion/images")
