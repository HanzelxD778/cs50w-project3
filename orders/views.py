#from django.core.checks import messages
from django.contrib.auth import models
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages #import messages
from django.contrib.auth.decorators import login_required
from . models import DetalleOrden, Orden, RegularPizza, ShoppingCart, SicilianPizza, Toppings, Subs, Pasta, Salads, DinnerPlatters
#from . models import Categorias

# Create your views here.
@login_required
def index(request):

    context = {
        "username": request.user,
        "RegularPizzas": RegularPizza.objects.all(),
        "SicilianPizzas": SicilianPizza.objects.all(),
        "Toppings": Toppings.objects.all(),
        "Subs": Subs.objects.all(),
        "Pastas": Pasta.objects.all(),
        "Salads": Salads.objects.all(),
        "DinnerPlatters": DinnerPlatters.objects.all(),
    }

    return render(request, 'orders/index.html', context)

def register(request):
    if request.method == "GET":
        return render(request, "orders/register.html")
    else:
        first_name = request.POST["firstName"]
        last_name = request.POST["lastName"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]

    if User.objects.filter(username=username).exists():
        return render(request, "orders/register.html", messages.error(request, "User already exists D:" ))

    #https://docs.djangoproject.com/en/3.2/topics/auth/default/
    user = User.objects.create_user(username, email, password)
    user.first_name = first_name
    user.last_name = last_name
    user.save()

    messages.success(request, "User saved." )

    return HttpResponseRedirect(reverse("login"))

def customize(request):
    if request.method == "POST":
        
        tabla = request.POST.get("nombre_tabla")
        name = request.POST.get("nombre_pizza")
        small = request.POST.get("precio_small")
        large = request.POST.get("precio_large")
        max_extras = request.POST.get("max_extras")

        context = {
            "tabla" : tabla,
            "name" : name,
            "small" : small,
            "large" : large,
            "max_extras": max_extras, 
            "Toppings": Toppings.objects.all(),
        }

        return render(request, "orders/customize.html", context)
    else:
        print("ENTRE POR GET A CUSTOMIZE")

def carrito(request):
    if request.method == "POST":
        price = request.POST.get("price")
        toppings = request.POST.getlist("toppings")
        nombre_tabla = request.POST.get("nombre_tabla")
        nombre_pizza = request.POST.get("nombre_pizza")
        max_extras = request.POST.get("max_extras")
        cantidad = request.POST.get("cantidad")

        #obtener orden del cliente cuyo estado esta en progreso
        orden = Orden.objects.filter(username=request.user, estado="0").first()

        if not orden:
            orden = Orden.objects.create(username=request.user, estado="0", total=0)

        detalle_orden = DetalleOrden.objects.create(orden=orden, producto=nombre_pizza, precio=price, cantidad=cantidad)

        try:
            #https://www.delftstack.com/es/howto/python/python-split-list-into-chunks/
            output=[toppings[i:i + int(max_extras)] for i in range(0, len(toppings), int(max_extras))]
            output1 = output[0]
        except:
            output=None
            output1=None
        
        print(output)
        print(output1)
 
        orden = f"{nombre_tabla} {nombre_pizza} {str(output1)[1:-1]}"
        
        context = {
            "user_order": ShoppingCart.objects.filter(username=request.user),
            "price": price,
            "orden" : orden,
        }

        new_order = ShoppingCart(username=request.user, order=orden, price=price, approved="pending")
        new_order.save()

        #aqui me falta hacer alguna validacion con respecto al total
        #orden = Orden(username=request.user, estado=0)
        #orden.save()

        #aqui no se como meter la lista de toppings
        #detalle_orden = DetalleOrden(orden=orden, producto=nombre_pizza, precio=price, cantidad=cantidad)

        return render(request, "orders/carrito.html", context)
    else:

        context = {
            "user_order": ShoppingCart.objects.filter(username=request.user)
        }

        print(context)

        return render(request, "orders/carrito.html", context)

def staff(request):
    username = request.user
    context = {
        "username": username,
        "shopping_cart": ShoppingCart.objects.all()
    }
    return render(request, "orders/staff.html", context)

def approve_order(request):
    estado_orden = request.POST.get("estado_orden")
    order = ShoppingCart.objects.get(pk=estado_orden)
    order.approved = "approved"
    order.save()
    return HttpResponseRedirect(reverse("staff"))