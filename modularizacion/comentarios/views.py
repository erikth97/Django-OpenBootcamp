
from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

def test(request):
    return HttpResponse("Funciona el envio de datos")
    
def create(request):
    # comment = Comment(name="ErikT", score=5, comment="Este es un comentario")
    # comment.save()
    comment = Comment.objects.create(name="Fabian")
    return HttpResponse("creacion de modelos")

def delete(request):
    # comment = Comment.objects.get(id=2)
    # comment.delete()
    Comment.objects.filter(id=3).delete()
    return HttpResponse("Ruta para probar los delete")