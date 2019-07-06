from django.db import models

# Create your models here.
class productos(models.Model):
    # id = models.CharField(max_length=3)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    talla = models.IntegerField( )
    cantidad = models.IntegerField( )
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=11, decimal_places=2)
    imagen = models.CharField(max_length=50)
    categoria = models.IntegerField( )
    subcategoria = models.IntegerField( )
    # PRIMARY KEY (id),
    # FOREIGN KEY (categoria) REFERENCES categorias(id),
    # FOREIGN KEY (subcategoria) REFERENCES subcategorias(id)

class subcategorias(models.Model):
    # id
    nombre = models.CharField(max_length=50)
    imagen = models.CharField(max_length=50)


class categorias(models.Model):
    # id                  INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre = models.CharField(max_length=50)
    imagen = models.CharField(max_length=50)

class Pedido_Detalle(models.Model):
    cantidad = models.IntegerField( )
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
