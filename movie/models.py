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
    promoted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["title"]


class MoviePoster(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="movie/images")


class VideoLink(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="links")
    link = models.URLField()


class SubcriptionType(models.Model):
    plan = models.CharField(max_length=255)
    monthly_price = models.PositiveBigIntegerField()
    video_quality = models.CharField(max_length=255)
    resolution = models.CharField(max_length=255)
    devices = models.CharField(default="Mobile", max_length=255)

    def __str__(self):
        return self.plan


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subscription = models.ForeignKey(SubcriptionType, on_delete=models.PROTECT)

    def first_name(self):
        return self.user.first_name


class WatchList(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user"
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
