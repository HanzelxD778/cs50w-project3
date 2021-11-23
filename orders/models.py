from django.db import models
from django.utils import tree

# Create your models here.
class Category(models.Model):
    STATUS = [("1", "Active"), ("0", "Deleted")]
    category = models.CharField(verbose_name="category of ", max_length=50)
    status = models.CharField(max_length=2, choices=STATUS, default="1")

    def __str__(self):
        return f"{self.category} {self.status}"

class Topping(models.Model):
    top = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.top}"

class saucer(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True),
    product = models.CharField(max_length=100, blank=True),
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True),
    small = models.DecimalField(max_digits=5, decimal_places=2, blank=True),
    large = models.DecimalField(max_digits=5, decimal_places=2, blank=True),
    top = models.PositiveIntegerField(blank=True, default=0)
    