# Generated by Django 4.1.1 on 2022-09-28 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0007_rename_dailyrentalrate_movie_imdbrating"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="numberInStock",
        ),
    ]
