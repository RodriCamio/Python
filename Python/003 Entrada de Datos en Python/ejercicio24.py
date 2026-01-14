# Entrada de Datos por Consola
# Estrucctura Base:
# variable = input("Mensaje para el usuario: ")

nombre = input("Por favor, ingresa tu nombre: ")
print("Hola, " + nombre + "! Bienvenido/a a Python.")

# La trampa del texto
# Por defecto, todo lo que se ingresa por consola es tratado como texto (string).
edad = input("Por favor, ingresa tu edad: ") # El usuaruio ingresa 25

# ¿Que pasa si intentamos sumar 5 a la edad?

# print(edad + 5)

# vamos a recibir un error de tipo (TypeError)
# TypeError: can only concatenate str (not "int") to str
# Esto sucede porque 'edad' es un string, no un número.

# Convertir el tipo de dato
# Para solucionar esto, necesitamos convertir 'edad' a un entero (int) o a un número de punto flotante (float).
edad_entero = int(edad)  # Convertimos la edad a entero
print("En 5 años, tendrás " + str(edad_entero + 5) + " años.")

# Para decimales (precio, altura, etc.)
altura = input("Por favor, ingresa tu altura en metros (por ejemplo, 1.75): ")
altura_flotante = float(altura)  # Convertimos la altura a float
print("Tu altura es de " + str(altura_flotante) + " metros.")

# Resumen:
# - input() siempre devuelve un string.
# - Usa int() para convertir a entero.
# - Usa float() para convertir a número decimal.
