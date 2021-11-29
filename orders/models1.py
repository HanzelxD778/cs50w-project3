from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categorias(models.Model):
    ESTADO = [("1", "Active"), ("0", "Deleted")]
    categoria = models.CharField(max_length=50)
    estado = models.CharField(max_length=10, choices=ESTADO, default="1")

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return f"{self.categoria} {self.estado}"

class Toppings(models.Model):
    topping = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Toppings"

    def __str__(self):
        return f"{self.topping}"

class Platillos(models.Model):
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, null=True)
    nombre_platillo = models.CharField(max_length=100, blank=True)
    precio = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    SIZE = [("1", "small"), ("2", "large")]
    size = models.CharField(max_length=10, choices=SIZE, default=1)
    numuero_toppings = models.PositiveIntegerField(blank=True, default=0)

    class Meta:
        verbose_name_plural = "Platillos"
    
    def __str__(self):
        return f"{self.categoria.categoria} {self.nombre_platillo} {self.size} {self.precio} {self.numuero_toppings}"

class CarritoDetalle(models.Model):
    platillo = models.ForeignKey(Platillos, on_delete=models.CASCADE, null=True)
    

class Carrito(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    producto = models.CharField(max_length=100, blank=True)
    extras = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=100, blank=True)
    amount = models.IntegerField(blank=True)
    amount_extras = models.IntegerField(blank=True)
    total = models.DecimalField(max_digits=5, decimal_places=2, blank=True)

    class Meta:
        verbose_name_plural = "Carrito"

    def __str__(self):
        return f"{self.cliente.username} {self.product} {self.extras} {self.size} {self.amount} {self.amount_extras} {self.total}"