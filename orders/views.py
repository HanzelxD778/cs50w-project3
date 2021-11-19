#from django.core.checks import messages
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages #import messages

# Create your views here.
def index(request):
    return render(request, 'orders/index.html')

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

    user = User.objects.create_user(username, email, password)
    user.first_name = first_name
    user.last_name = last_name
    user.save()

    messages.success(request, "User saved." )

    return HttpResponseRedirect(reverse("login"))