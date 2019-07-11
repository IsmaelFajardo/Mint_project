from django.urls import path
from catalogo import views

urlpatterns = [
    path('', views.index, name='index'),
    path("catalogo/productos", views.catalogo, name="catalogo"),
    path("catalogo/productos/<int:idProducto>", views.producto, name="producto"),
]
