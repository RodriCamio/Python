# Concatenar cadenas de texto en Python

# Definir dos cadenas de texto
cadena1 = "Hola,"
cadena2 = "mundo!"

# Concatenar las dos cadenas
cadena_concatenada = cadena1 + " " + cadena2

# Imprimir el resultado
print(cadena_concatenada)  # Salida: Hola, mundo!
print("Ejemplo de concatenacion: " + cadena1 + " " + cadena2)  # Salida: Hola, mundo! 

# Otra forma de concatenar usando f-strings
print(f"Ejemplo de concatenacion: {cadena1} {cadena2}")  # Salida: Hola, mundo!

# Podemos realizar operaciones adicionales con las cadenas concatenadas
nombre = "Alice"
edad = 30
ciudad = "Madrid"
print(f"{nombre} tiene {edad + 1} años y vive en {ciudad}.")  # Salida: Alice tiene 31 años y vive en Madrid.