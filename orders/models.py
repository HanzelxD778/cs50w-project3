from django.db import models

# Create your models here.
class Tipo(models.Model):
    tipo = models.CharField(verbose_name="tipo de pizza", max_length=30)

    def __str__(self):
        return f"{self.tipo}"