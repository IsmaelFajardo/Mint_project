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
    #identificador = productos.objects.get(id)
    p = productos.objects.get(pk=idProducto)
    return render(request, "catalogo/producto.html",
        {
        "producto": p
        })


# def productos(request):
#     """vista para atender la petición de la url catalogo/productos"""
#     nombre = productos.objects.all()
#     precio = productos.objects.all()
#
#     return render(request, "catalogo/catalogo.html",
#         {
#         "nombre": nombre,
#         "precio": precio
#         }
#     )


# if request.method == "POST":
#     idProductos = request.POST["idProductos"]
#     idProductos = int(x=idProductos)
#     idProducto1 = request.POST["idProducto1"]
#     idProducto2 = request.POST["idProducto2"]
