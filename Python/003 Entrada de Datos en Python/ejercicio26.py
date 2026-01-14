# Receta de Cocina

# Crear un programa para solicitar algunos valores importantes para una receta de cocina.
# Los valores que debe introducir el usuario son:
# - Nombre de la receta
# - Ingredientes
# - Tiempo de preparación (en minutos)
# - Dificultad (fácil, medio, difícil)

# Mandar a imprimir un resumen de la receta con los datos introducidos por el usuario.

print("=== Receta de Cocina ===")
nombre_receta = input("Nombre de la receta: ")
ingredientes = input("Ingredientes: ")
tiempo_preparacion = int(input("Tiempo de preparación (en minutos): "))
dificultad = input("Dificultad (fácil, medio, difícil): ")

print("-"*30)
print(f"Nombre: {nombre_receta}")
print(f"Ingredientes: {ingredientes}")
print(f"Tiempo de preparación: {tiempo_preparacion} minutos")
print(f"Dificultad: {dificultad}")