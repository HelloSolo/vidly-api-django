from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Genre(models.Model):
    title = models.CharField(max_length=255)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    numberInStock = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    dailyRentalRate = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )
