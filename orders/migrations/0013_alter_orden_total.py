# Generated by Django 3.2 on 2021-12-03 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_shoppingcart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='total',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]