from django.db import models

# Create your models here.
class productos(models.Model):
    # id = models.CharField(max_length=3)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    talla = models.SmallIntegerField()
    cantidad = models.SmallIntegerField( )
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=11, decimal_places=2)
    imagen = models.ImageField()
    categoria  = [
        ("Mujer", "Mujer"),
        ("Hombre", "Hombre"),
    ]
    categoria = models.CharField(max_length=50, choices=categoria)
    subcategoria  = [
        ("business", "business"),
        ("casual", "casual"),
        ("chamarra", "chamarra"),
        ("shoes", "shoes"),
        ("tshirt", "tshirt"),
    ]
    subcategoria = models.CharField(max_length=50, choices=subcategoria)


class subcategorias(models.Model):
    # id
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField( blank=True)
    # imagen = models.ImageField(upload_to=’product_photo’, blank=True)


class categorias(models.Model):
    # id                  INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField( blank=True)

class Pedido_Detalle(models.Model):
    cantidad = models.SmallIntegerField( )
    subtotal = models.DecimalField(max_digits=11, decimal_places=2)
    pedido = models.IntegerField( )
    producto = models.CharField(max_length=50)
    # FOREIGN KEY (pedido) REFERENCES pedidos(id),
    # FOREIGN KEY (producto) REFERENCES productos(id)

# class Catalog(models.Model):
#     name = models.CharField(max_length=255)
#     slug=models.SlugField(max_length=150)
#     publisher=models.CharField(max_length=300)
#     description=models.TextField()
#
# class Product(models.Model):
#     name=models.ForeignKey(Catalog, on_delete=models.CASCADE)
#     slug=models.SlugField(max_length=150)
#     description=models.TextField()
#     # photo=models.ImageField(upload_to=’product_photo’, blank=True)
#     price_in_dollars=models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        """ se define la representación en str para Producto """
        return str(self.id)
