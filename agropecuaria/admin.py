from django.contrib import admin
from .models import Ventas, Producto, Cliente

# Register your models here.
admin.site.register(Ventas)
admin.site.register(Producto)
admin.site.register(Cliente)
