from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ManyToManyField

# Create your models here.
class RegularPizza(models.Model):
    name = models.CharField(max_length=15)
    small = models.CharField(max_length=5)
    large = models.CharField(max_length=5)
    max_extras = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} {self.small} {self.large}"

class SicilianPizza(models.Model):
    name = models.CharField(max_length=15)
    small = models.CharField(max_length=5)
    large = models.CharField(max_length=5)
    max_extras = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} {self.small} {self.large}"

class Toppings(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Toppings"
    
    def __str__(self):
        return f"{self.name}"

class Subs(models.Model):
    name = models.CharField(max_length=60)
    small = models.CharField(max_length=5, blank=True)
    large = models.CharField(max_length=5, blank=True)

    class Meta:
        verbose_name_plural = "Subs"

    def __str__(self):
        return f"{self.name} {self.small} {self.large}"

class Pasta(models.Model):
    name = models.CharField(max_length=40)
    price = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.name} {self.price}"

class Salads(models.Model):
    name = models.CharField(max_length=40)
    price = models.CharField(max_length=5)

    class Meta:
        verbose_name_plural = "Salads"

    def __str__(self):
        return f"{self.name} {self.price}"

class DinnerPlatters(models.Model):
    name = models.CharField(max_length=40)
    small = models.CharField(max_length=5)
    large = models.CharField(max_length=5)

    class Meta:
        verbose_name_plural = "DinnerPlatters"

    def __str__(self):
        return f"{self.name} {self.small} {self.large}"

class Orden(models.Model):
    username = models.ForeignKey(User, on_delete=CASCADE, related_name="carrito")
    total = models.FloatField(blank=True, null=True)
    ESTADO = [("0", "progreso"), ("1", "finalizado"), ("2", "cancelado")]
    estado = models.CharField(max_length=10, choices=ESTADO, default="0")
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Orden"

    def __str__(self):
        return f"{self.username} {self.total} {self.estado} {self.fecha}"

class DetalleOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=CASCADE, related_name="orden_detalle")
    producto = models.CharField(max_length=60)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    toppingsList = ManyToManyField(Toppings, related_name="detalle_ordenes", blank=True)

    class Meta:
        verbose_name_plural = "DetalleOrden"

    def __str__(self):
        return f"{self.orden} {self.producto} {self.precio} {self.cantidad} {self.toppingsList}"

class ShoppingCart(models.Model):
    username = models.CharField(max_length=25)
    order = models.CharField(max_length=100)
    price = models.FloatField(blank=True, null=True)
    approved = models.CharField(max_length=10, default="None")

    def __str__(self):
        return f"{self.username} {self.order} {self.price} {self.approved}"