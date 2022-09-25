from django.urls import path
from .views import create_user, login

urlpatterns = [path("users/", create_user), path("auth/", login)]
