from django.shortcuts import render
from .models import productos


# Create your views here.

def index(request):
    """ Vista para atender la petición de la url / """
    return render(request, "catalogo/index.html")


def catalogo(request):
    """ Vista para atender la petición de la url /catalogo hombre """
    prods = productos.objects.all()
    return render(request, "catalogo/catalogo.html",
        {
        "productos": prods
        })


def producto(request, idProducto):
    """ Vista para atender la petición de la url  producto chamarra hombre/ """
    p = productos.objects.get(pk=idProducto)
    return render(request, "catalogo/producto.html",
        {
        "producto": p
        })
