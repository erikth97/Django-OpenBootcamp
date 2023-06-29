from django.http import HttpResponse

def saludo(request):
    return HttpResponse("django")

def despedida(request):
    return HttpResponse("OpenBootcamp")