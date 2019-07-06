from django.urls import path
from catalogo import views

urlpatterns = [
    path('', views.index, name='index'),
    path("catalogo", views.catalogo, name="catalogo"),
    path("catalogo", views.producto, name="producto"),
]
