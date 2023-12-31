from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")
def gino(request):
    return HttpResponse("Hello, Gino!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")