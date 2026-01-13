# Sistema de tienda online

# Crear el detalle de un producto de una tienda online
# El detalle debe incluir:
# - Nombre del producto
# - Precio
# - Cantidad en stock
# - Indicar si esta disponible
# Ademas, debe hacer algunos cambios y mandar a imprimir nuevamente el nuevo valor de las variables.

# Definición del producto
nombre_producto = "Auriculares Inalámbricos"
precio = 59.99
cantidad_en_stock = 25
disponible = True

# Imprimir detalles del producto
print("=== Detalle del Producto: ===")
print("Producto:", nombre_producto)
print("Precio: $", precio)
print("Cantidad en stock:", cantidad_en_stock)
print("Disponible:", disponible)

# Realizar algunos cambios
precio = 49.99  # Cambio de precio
cantidad_en_stock = 0  # Actualización de stock
disponible = False  # Actualización de disponibilidad

# Imprimir detalles actualizados del producto
print("\n=== Detalle del Producto Actualizado: ===")
print("Producto:", nombre_producto)
print("Precio: $", precio)
print("Cantidad en stock:", cantidad_en_stock)
print("Disponible:", disponible)