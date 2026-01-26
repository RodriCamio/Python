# Valor dentro de Rango

# Solicitar al usuario un valor entre 0 y 5 e indicarle si el valor proporcionado esta dentro de rango. 
# Se deben definir 2 constantes, VALOR_MINIMO = 0 y VALOR_MAXIMO = 5
# Y debemos comprobar si el valor proporcionado se encuentra en el rango entre 0 y 5.
# Finalmente se debe imprimir:
# Valor dentro del rango: True o False.

print('=== Valor dentro de rango ===')

# Creamos los limites:
VALOR_MINIMO = 0
VALOR_MAXIMO = 5

# Solicitamos el numero al usuario
valor = int(input(f'\nIngrese un numero entre {VALOR_MINIMO} y {VALOR_MAXIMO}: '))

# Respuesta
print(f'\nEsta dentro del rango?: {VALOR_MINIMO <= valor <= VALOR_MAXIMO}')
