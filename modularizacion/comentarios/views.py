from django.shortcuts import render
from django.http import HttpResponse


def test(request):
    return HttpResponse("Funciona el envio de datos")
    
def create(request):
    return HttpResponse("creacion de modelos")