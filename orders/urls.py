from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("customize", views.customize, name="customize"),
    path("carrito", views.carrito, name="carrito"),
    path("staff", views.staff, name="staff"),
    path("approve_order", views.approve_order, name="approve_order"),
]
