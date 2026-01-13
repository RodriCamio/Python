# Sistema de Reserva de Hoteles

# Crear un sistema de reseva de hoteles utilizando variables para almacenar la información relevante.
# Nombre del cliente, dias de estancia, tarifa diaria, indicar si el cuarto tiene vista al mar (booleano), calcular el costo total de la estancia.
# Despues mandar a imprimir los valores de cada variable
# Hacer algunos cambios y re-imprimir los valores actualizados.

# Información del cliente
nombre_cliente = "Ana García"
dias_estancia = 5
tarifa_diaria = 120.50
vista_al_mar = True

# Imprimir la información inicial
print("=== Reserva de Hotel ===")
print("Nombre del Cliente:", nombre_cliente)
print("Días de Estancia:", dias_estancia)
print("Tarifa Diaria: $", tarifa_diaria)
print("Vista al Mar:", vista_al_mar)

# Modificar algunos valores
nombre_cliente = "Ana María García"
dias_estancia = 7
tarifa_diaria = 110.00
vista_al_mar = False

# Re-imprimir la información actualizada
print("\n=== Reserva de Hotel Actualizada ===")
print("Nombre del Cliente:", nombre_cliente)
print("Días de Estancia:", dias_estancia)
print("Tarifa Diaria: $", tarifa_diaria)
print("Vista al Mar:", vista_al_mar)