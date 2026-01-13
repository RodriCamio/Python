# Reemplazar Subcadenas en Python

# ¿Que es replace?
# El método replace() en Python se utiliza para reemplazar todas las ocurrencias de una subadena
# dentro de una cadena por otra subcadena especificada. Este método devuelve una nueva cadena.

# Sintaxis:
# cadena.replace(subcadena_vieja, subcadena_nueva, [num_reemplazos])

# Programa: Reemplazar textos en python
frase = "Hola Mundo, Mundo"

# Reemplazar todas las apariciones
nuevo = frase.replace("Mundo", "Python")
print(nuevo)  # Imprime: "Hola Python, Python"

# Reemplazar solo la primera aparición
uno_solo = frase.replace("Mundo", "Python", 1)
print(uno_solo)  # Imprime: "Hola Python, Mundo"