# Ejemplo de uso de asignacion multiple puede ser la inversion de valores entre dos variables.

# Supongamos que tenemos dos variables con valores iniciales.
a, b = 5, 10
print(f'Antes de la inversion: a = {a}, b = {b}') # Salida: Antes de la inversion: a = 5, b = 10

# Usando asignacion multiple para intercambiar los valores.
a, b = b, a
print(f'Despues de la inversion: a = {a}, b = {b}') # Salida: Despues de la inversion: a = 10, b = 5

# Recibir multiple  valores de la entrada del usuario.
nombre, apellido = input("Ingresa tu nombre y apellido separados por comas: ").split(',')
print(f'Nombre: {nombre.strip()}, Apellido: {apellido.strip()}')