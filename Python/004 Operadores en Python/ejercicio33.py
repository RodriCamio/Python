# Operadores de Asignacion compuestos

# Los operadores de asignación compuestos combinan una operación aritmética con la asignación.

# Los operadores pueden ser: +=, -=, *=, /=, //=, %=, **=

# Sintaxis:
# variable operador valor

print("=== Operadores de Asignacion compuestos ===")
x = 100
print(f"El valor inicial de x es {x}")
# Ejemplo de suma con asignación compuesta:
x += 5  # x = x + 5
print(f'El resultado de x += 5 es {x}')  # Salida: 15

# Ejemplo de resta con asignación compuesta:
x -= 3  # x = x - 3
print(f'El resultado de x -= 3 es {x}')  # Salida: 12

# Ejemplo de multiplicación con asignación compuesta:
x *= 2  # x = x * 2
print(f'El resultado de x *= 2 es {x}')  # Salida: 24

# Ejemplo de división con asignación compuesta:
x /= 4  # x = x / 4
print(f'El resultado de x /= 4 es {x}')  # Salida: 6.0

# Ejemplo de división entera con asignación compuesta:
x //= 2  # x = x // 2
print(f'El resultado de x //= 2 es {x}')  # Salida: 3.0

# Ejemplo de módulo con asignación compuesta:
x %= 2  # x = x % 2
print(f'El resultado de x %= 2 es {x}')  # Salida: 1.0

# Ejemplo de potencia con asignación compuesta:
x **= 3  # x = x ** 3
print(f'El resultado de x **= 3 es {x}')  # Salida: 1.0

print("=== Fin del programa ===")