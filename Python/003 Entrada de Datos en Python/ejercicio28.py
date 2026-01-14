# Sistema Generador ID Unicos

# Se solicita crear un sistema para generar un ID unico para cada persona.

# El sistema debe solicitar al usuario:
# - Nombre
# - Apellido
# - Año de nacimiento (yyyy)

# Con esos datos recibidos el sistema debera realizar lo siguiente:
# 1. Del valor recibido de nombre, usar solo los 2 primeras letras, y convertirlas a mayusculas.
# 2. Del valor recibido de apellido, usar solo las 2 primeras letras, y convertirlas a mayusculas.
# 3. Del valor recibido de año de nacimiento, usar solo los 2 ultimos digitos.

# Ademas el sistema debera un valor aleatorio de 4 digitos, con ayuda de la funcion randint.
# Finalemnte, con los datos obtenidos generar un id unico unendo los valores como sigue:
# Ejemplo: Nombre: Juan, Apellido: Perez, Año Nacimiento: 1990, valor aleatorio: 1234
# ID unico: JUPE901234

print("=== Generador de ID Unico ===")  
from random import randint
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
nacimiento = input("Ingrese su año de nacimiento (yyyy): ")
aleatorio = randint(1000, 9999)
id_unico = nombre[:2].upper() + apellido[:2].upper() + nacimiento[-2:] + str(aleatorio)
print("-"*30)
print(f"Su ID unico es: {id_unico}")

