from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request): # request: <WSGIRequest: GET '/'>
    return HttpResponse("<strong>Hola</strong> mundo!")
