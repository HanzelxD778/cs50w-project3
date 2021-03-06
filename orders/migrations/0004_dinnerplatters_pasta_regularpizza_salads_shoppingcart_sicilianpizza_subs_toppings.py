# Generated by Django 3.2 on 2021-11-28 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0003_auto_20211127_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='DinnerPlatters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('small', models.CharField(max_length=5)),
                ('large', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name_plural': 'DinnerPlatters',
            },
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('price', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='RegularPizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('small', models.CharField(max_length=5)),
                ('large', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Salads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('price', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name_plural': 'Salads',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('order', models.CharField(max_length=100)),
                ('price', models.FloatField(blank=True, null=True)),
                ('toppingsList', models.CharField(default='', max_length=100)),
                ('approved', models.CharField(default='None', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SicilianPizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('small', models.CharField(max_length=5)),
                ('large', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Subs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('small', models.CharField(max_length=5)),
                ('large', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name_plural': 'Subs',
            },
        ),
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Toppings',
            },
        ),
    ]
