from django.contrib import admin
from .models import productos, subcategorias, categorias, Pedido_Detalle

# Register your models here.
admin.site.register(productos)
#
# class ProductosAdmin(admin.ModelAdmin):
#     # Se sobre escribe lo que hace __str__
#     list_display = ("id", "marca", "modelo", "talla", "cantidad", "nombre", "precio", "imagen", "categoria", "subcategoria")
#     admin.site.register(Productos, ProductosAdmin)
#
# class SubcategoriasAdmin(admin.ModelAdmin):
#     list_display = ("nombre", "imagen")
#     admin.site.register(Subcategorias, SubcategoriasAdmin)
#
# class CategoriasAdmin(admin.ModelAdmin):
#     list_display = ("nombre", "imagen")
#     admin.site.register(Categorias, CategoriasAdmin)
#
# class Pedido_Detalle(admin.ModelAdmin):
#     list_display = ("cantidad", "subtotal",  "pedido", "producto")
#     admin.site.register(Pedido_Detalle, Pedido_DetalleAdmin)
