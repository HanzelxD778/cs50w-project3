# Project 3

En este proyecto, se construyó una aplicación web que maneja las órdenes en línea de un restaurante de pizza. Los usuarios son ser capaces de navegar en el menú del restaurante, agregar items a sus carritos de compras, y confirmar sus órdenes. Mientras tanto, los dueños del restaurante son capaces de añadir y actualizar los ítems del menú, y ver las órdenes que han sido solicitadas.

Existen 6 categorias:

Regular Pizza
Sicilian Pizza
Subs
Pastas
Salads
Dinner Platters

Cada categoria es una tabla en la base de datos, aparte de la tabla de los toppings que se agregan.

También contiene una tabla Ordenes y una DetalleOrdenes para almacenar lo que compra el usuario, una Orden puede tener muchos DetalleOrden y un DetalleOrden pertenece a una Orden

El toque personal de la aplicación es que el cliente puede ver el estado de su orden si la orden esta generada, si ya esta aprobada, si fue cancelada.

La orden se mantiene en estado creada, mientras no este generada todavía para que los propietarios del restaurante la aprueben.

Cuando entramos a la página luego de logearnos, podemos ver el menu, los platillos que pueden personalizarse como escogerla grande o pequeña, que toppings desea tener tienen el boton 'customize' y pueden ser agregadas al carrito, los platillos que no se pueden personalizar solamente muestran el precio del plato una vez seleccionado se agrega al carrito, ese carrito se genera con el boton de 'generate order' desde el apartado de carrito.

Cuenta de admin:
admin
get_pizza123

Cuenta con usuario comun:
a1
a1