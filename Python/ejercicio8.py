# Constantes en Python
# En Python, las constantes se definen utilizando variables con nombres en mayúsculas.

print("Definiendo constantes en Python")

# Definición de constantes
PI = 3.14159
print("Valor de PI:", PI)

NOMBRE_DEL_DIA = "Lunes"
print("Nombre del día:", NOMBRE_DEL_DIA)

# Esto NO se debe hacer, pero Python no lo impide
NOMBRE_DEL_DIA = "Martes"
print("Nuevo nombre del día (no recomendado):", NOMBRE_DEL_DIA)

# Buenas prácticas: Usar constantes para valores que no deben cambiar

# Usar una constalte del lenguaje Python, aunque en este caso no esta en mayusculas
import math
print('Valor de math.pi:', math.pi)