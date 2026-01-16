# Operadores en Python

# Los operadores son simbolos especiales que estan diseñados para realizar operaciones especificas. Tenemos varios tipos, como son:
# - Aritméticos: +, -, *, /, %, //, **
#   - Permiten realizar calculos matematicos basicos, como suma, resta, multiplicacion, division, modulo, division entera y exponenciacion.

# - De asignación: =, +=, -=, *=, /=, %=, //=, **=
#   - Se utilizan para asignar valores a las variables y para actualizar esos valores.

# - De comparación: ==, !=, >, <, >=, <=
#   - Permiten comparar dos valores y devuelven un valor booleano (True o False) dependiendo del resultado de la comparación.

# - Lógicos: and, or, not
#   - Se utilizan para combinar expresiones condicionales o logicas.

# - De identidad: is, is not
#   - Permiten comparar si dos objetos son el mismo en memoria.

# - De membresía: in, not in
#   - Se utilizan para verificar si un valor o variable existe dentro de una secuencia (como listas, tuplas o cadenas).

# Ejemplo de uso de operadores aritmeticos en Python
a = 5
b = 3

# Suma de dos numeros: 
suma = a + b
print("La suma de", a, "y", b, "es:", suma)

# Resta de dos numeros:
resta = a - b
print("La resta de", a, "y", b, "es:", resta)

# Multiplicacion de dos numeros:
multiplicacion = a * b
print("La multiplicacion de", a, "y", b, "es:", multiplicacion)

# Division de dos numeros: 
division = a / b
print(f"La division de {a} y {b} es: {division:.2f}")

# Modulo de dos numeros: 
modulo = a % b
print("El modulo de", a, "y", b, "es:", modulo)

# Division entera de dos numeros:
division_entera = a // b
print("La division entera de", a, "y", b, "es:", division_entera)

# Exponenciacion de dos numeros: 
exponenciacion = a ** b
print("La exponenciacion de", a, "elevado a", b, "es:", exponenciacion)