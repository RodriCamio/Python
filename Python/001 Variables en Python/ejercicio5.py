# Ejemplo reglas y buenas prácticas en Python

# Asignar valores a las variables:
nombre_explorador = "Lara Croft"    # Usar minúsculas y guiones bajos para separar palabras
edad_explorador = 28                # Nombres descriptivos y claros
planeta_origen = "Tierra"
nivel_energia = 75.0

# for = 15           # esto arroja error porque 'for' es una palabra reservada en Python
Nivel_Energia = 80   # No usar mayúsculas al inicio de nombres de variables
NIVEL_ENERGIA = 90   # No usar mayúsculas completas para nombres de variables
nivel_energia = 100  # Evitar reasignar variables con diferentes tipos de datos

# Imprimir la información almacenada en las variables
print("=== Ficha del Explorador ===")
print("Nombre del Explorador:", nombre_explorador)
print("Edad del Explorador:", edad_explorador)
print("Planeta de Origen:", planeta_origen)
print("Nivel de Energía:", nivel_energia)