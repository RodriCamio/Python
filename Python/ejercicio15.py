# Inmutabilidad de cadenas en Python

animal = "perro"

# animal[0] = "g"  # Esto generará un error porque las cadenas son inmutables
# print(animal)

# Correcto: Concatenar
# Tomamos "perro" + "s"

plural = animal + "s"
print(animal)  # Salida: perro
print(plural)  # Salida: perros

plural = f"{animal}ss"
print(plural)  # Salida: perross