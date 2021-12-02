from django.contrib import admin
from django.utils.translation import to_language
from .models import RegularPizza, ShoppingCart, SicilianPizza, Toppings, Subs, Pasta, Salads, DinnerPlatters, Orden, DetalleOrden

# Register your models here.
admin.site.register(RegularPizza)
admin.site.register(SicilianPizza)
admin.site.register(Toppings)
admin.site.register(Subs)
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(DinnerPlatters)
admin.site.register(Orden)
admin.site.register(DetalleOrden)
admin.site.register(ShoppingCart)