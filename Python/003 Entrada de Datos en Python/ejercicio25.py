# Sistema  de empleados

# Crea un programa para solicitar la informacino de un empleado, introduciendo los datos por cosola
# Nombre
# Edad (convertir a entero)
# Salario (convertir a float)
# Es Jefe de departamento (True/False)

print("=== Sistema de Empleados ===")
nombre = input("Nombre del empleado: ")
edad = int(input("Edad del empleado: "))
salario = float(input("Salario del empleado: "))
es_jefe_departamento = input("¿Es jefe de departamento? (Si/No): ").lower() == "si"

print("\n--- Información del Empleado ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Salario: ${salario:.2f}") # Formatear a 2 decimales ".2f"
print(f"Es jefe de departamento: {es_jefe_departamento}")