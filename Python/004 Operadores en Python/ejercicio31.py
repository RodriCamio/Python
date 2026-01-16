# Operadores de Asignación en Python

# El operador de asignacion se utiliza para asignar valores a las variables.
# El operador de asignacion basico es el signo igual (=).

# Sintaxis:
# variable = valor  
# Ejemplo:
numero = 10
texto = "Hola, Mundo!"
print(f'El valor de numero es: {numero}')  # Salida: 10
print(f'El valor de texto es: {texto}')   # Salida: Hola, Mundo!

# En Python tambien tenemos la asignacion multiple, que permite asignar valores a varias variables en una sola linea.
# Sintaxis:
# var1, var2, var3 = valor1, valor2, valor3
# Ejemplo:
a, b, c = 10, 'Hola', 3.5
print(f'El valor de a es: {a}')  # Salida: 10
print(f'El valor de b es: {b}')  # Salida: Hola
print(f'El valor de c es: {c}')  # Salida: 3.5

# En Python tambien contamos con la asignacion encadenada, que permite asignar el mismo valor a varias variables.
# Sintaxis:
# var1 = var2 = var3 = valor
# Ejemplo:
x = y = z = 100
print(f'El valor de x = {x}; y = {y}; z = {z}')  # Salida: 100