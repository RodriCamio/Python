# Convertir a mayúsculas todas las letras de una cadena dada en Python.

# ¿Para que sirve?
# Esta función es útil cuando se desea estandarizar el formato de texto,
# por ejemplo, para comparaciones de cadenas sin importar el caso,
# o para resaltar títulos y encabezados en mayúsculas.

# "Admin" == "admin"  # Falso
# ejemplo:
cadena = "PyThOn Es GeNiAl"

# Convertir la cadena a mayúsculas
cadena_mayusculas = cadena.upper()
print(cadena_mayusculas)  # Salida: "PYTHON ES GENIAL"

# Explicación:
# La función upper() convierte todos los caracteres de la cadena a mayúsculas.

# Convertir la cadena a minúsculas
cadena_minusculas = cadena.lower()
print(cadena_minusculas)  # Salida: "python es genial"

# Explicación:
# La función lower() convierte todos los caracteres de la cadena a minúsculas.

