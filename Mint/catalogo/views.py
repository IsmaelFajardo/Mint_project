# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    """ Vista para atender la petición de la url / """
    return render(request, "catalogo/index.html")
def catalogo(request):
    """ Vista para atender la petición de la url /catalogo hombre """
    return render(request, "catalogo/catalogo.html")
def producto(request):
    """ Vista para atender la petición de la url  producto chamarra hombre/ """
    return render(request, "catalogo/producto.html")


def productos(request):
    """vista para atender la petición de la url catalogo/productos"""
    nombre = productos.objects.all()
    precio = productos.objects.all()

    return render(request, "catalogo/catalogo.html",
        {
        "nombre": nombre,
        "precio": precio
        }
    )


# if request.method == "POST":
#     idProductos = request.POST["idProductos"]
#     idProductos = int(x=idProductos)
#     idProducto1 = request.POST["idProducto1"]
#     idProducto2 = request.POST["idProducto2"]
