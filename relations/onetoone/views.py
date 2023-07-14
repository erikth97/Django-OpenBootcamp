from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant

def create(request):
    place = Place(name="Lugar 1", address="Calle Demo")
    return HttpResponse("Datos creados")
