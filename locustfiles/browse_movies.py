from locust import HttpUser, task
from random import randint


class WebsiteUser(HttpUser):
    @task
    def view_movies(self):
        self.client.get("/api/movies", name="/api/movies")

    @task
    def view_movie(self):
        movie_id = randint(14, 27)
        self.client.get(f"/api/movies/{movie_id}", name="/api/movies/:id")
