# Generated by Django 3.2 on 2021-11-30 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0004_dinnerplatters_pasta_regularpizza_salads_shoppingcart_sicilianpizza_subs_toppings'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarritoOrdenes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('0', 'cancelado'), ('1', 'espera'), ('2', 'realizado')], default='1', max_length=10)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carrito', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleOrden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.FloatField()),
                ('cantidad', models.IntegerField()),
                ('approved', models.BooleanField(default=False)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='orders.carritoordenes')),
                ('toppingsList', models.ManyToManyField(blank=True, related_name='detalle_ordenes', to='orders.Toppings')),
            ],
        ),
        migrations.DeleteModel(
            name='ShoppingCart',
        ),
    ]
