#from django.core.checks import messages
from django.contrib.auth import models
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages #import messages
from django.contrib.auth.decorators import login_required
from . models import RegularPizza, SicilianPizza, Toppings, Subs, Pasta, Salads, DinnerPlatters
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

        context = {
            "tabla" : tabla,
            "name" : name,
            "small" : small,
            "large" : large,
            "Toppings": Toppings.objects.all(),
        }
        
        return render(request, "orders/customize.html", context)
    else:
        return render(request, "orders/customize.html")