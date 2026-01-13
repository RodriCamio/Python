# Multiplicacion de cadenas en Python

# Las Matematicas se pueden convinar con las cadenas de texto en Python.
# La formula: "cadena" * Entero 

texto = "Na " * 8 + "Batman!"
print(texto)  # Imprime: "Na Na Na Na Na Na Na Na Batman!"

# ¡Cuidado! Multiplicar una cadena por un número negativo o por cero resulta en una cadena vacía.
texto_vacio = "Hola" * 0
print(f"Cadena vacía: '{texto_vacio}'")  # Imprime: "Cadena vacía: ''"

# 1. Crear un separador visual
linea = "-" * 30
print(linea)  # Imprime una línea de 30 guiones: "------------------------------

# 2. Identacion simple
nivel = 4
sangria = " " * nivel  # Crea una sangría de 2 espacios
print(f"{sangria}Este texto está indentado.")  # Imprime el texto con sangría

# 3. Repetir un patrón
patron = "*-" * 5
print(patron)  # Imprime: "*-*-*-*-*-"

# 4. Error comun
# texto_flotante = "hola" * 2.5  # Esto generará un error de tipo
# TypeError: can't multiply sequence by non-int of type 'float'