# Generated by Django 4.1.1 on 2022-10-05 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0016_movie_promoted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="watchList",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="movie",
                to="movie.movie",
            ),
        ),
    ]
