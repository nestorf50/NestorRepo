from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100)
    telefono = models.PositiveIntegerField()
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return "Nombre cliente: "+self.nombre_cliente

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto=models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return "Nombre producto: "+self.nombre_producto

class Ventas(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return "Cantidad vendida: "+ str(self.cantidad)
