from django.shortcuts import render
from django.http import HttpResponseRedirect
from pprint import pprint

# Create your views here.
def create_user(request):
    return HttpResponseRedirect("http://127.0.0.1:8000/auth/users")


def login(request):
    return HttpResponseRedirect("http://127.0.0.1:8000/auth/jwt/create")
