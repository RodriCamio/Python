# El Mayor de 2 numeros

# Crear un programa para indicar cual es el mayor de dos numeros.

# El programa debe pedir al usuario dos numeros enteros.

# Posteriormente se deben comparar y mandar a imprimir el numero mayor.

print('=== El Mayor de 2 numeros ===')

# Solicitamos 2 numeros enteros
numero1 = int(input('Ingrese el primer numero entero: '))
numero2 = int(input('Ingrese el segundo numero entero: '))

# Comparamos
mayor = numero1 if numero1 >= numero2 else numero2

# Resultado
print(f'\nEl numero que es mayor es: {mayor}\n')

# Fin del programa
print('=== Fin del programa ===')