from django.apps import AppConfig


class MovieConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "movie"

    def ready(self) -> None:
        import movie.signals

        return super().ready()
