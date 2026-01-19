# Sistema Descuentos VIP

# Una tienda de supermercado ofrece un descuento especual a clientes que compren 10 o mas articulos por dia Y ademas sean miembros de la tienda.
# El sistema debe solicitar al cliente que indique cuantos articulos ha comprado en el dia y preguntarle si cuenta con la membresia de la tienda.
# En caso de haber comprado 10 o mas productos y ser miembro de la tienda entonces tendra acceso al descuento

print("=== Sistema Descuentos VIP ===")
NO_PRODUCTOS_DESCUENTO = 10 # Definimos la cantidad de productos necesaria para el descuento.
cantidad_productos = int(input('¿Cuantos productos compraste hoy?: ')) # Consultamos al usuario la cantidad de productos que compro hoy.
tiene_membresia = input('¿Usted cuenta con la membresia de la tienda (si/no): ') # Consultamos si el usuario tiene la membresia de la tienda.

aplica_descuento = (cantidad_productos >= NO_PRODUCTOS_DESCUENTO) and (tiene_membresia.strip().lower() == 'si') # Usamos el operador AND para comparar los valores y determinar si es verdadero o no. 

print(f'¿Tienes acceso al descuento VIP?: {aplica_descuento}')