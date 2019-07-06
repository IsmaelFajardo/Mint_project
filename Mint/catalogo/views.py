# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    """ Vista para atender la petición de la url / """
    return render(request, "catalogo/index.html")
def catalogo(request):
    """ Vista para atender la petición de la url /catalogo """
    return render(request, "catalogo/catalogo.html")
def producto(request):
    """ Vista para atender la petición de la url / """
    return render(request, "catalogo/producto.html")
