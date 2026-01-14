# Generar Valores aleatorios

# La funcion randint() del módulo random nos permite generar números enteros aleatorios dentro de un rango específico.
# randint(a, b) devuelve un número aleatorio entre a y b, ambos inclusive.

# Es necesario importar en primer lgar el modulo random antes de usar la funcion randint().

# Para importar el modulo random, usamos la siguiente instruccion:
# import random
from random import randint # Importamos solo la funcion randint del modulo random

# Generamos un número aleatorio entre 1 y 10
numero_aleatorio = randint(1, 10)
print(f"Número aleatorio entre 1 y 10: {numero_aleatorio}")

# Simular un dado de seis caras
dado = randint(1, 6)
print(f"Resultado del lanzamiento del dado: {dado}")


