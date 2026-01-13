# Busqueda de subcadenas en Python

# Buscar subcadenas (find): El metodo find() devuelve el índice de la primera aparición
# de una subcadena dentro de una cadena. Si no se encuentra, devuelve -1.

cadena = "Hola mundo, bienvenido al mundo de Python."
posicion = cadena.find("mundo")
print(f"La subcadena 'mundo' se encuentra en la posición: {posicion}")  # Imprime: La subcadena 'mundo' se encuentra en la posición: 5

# Obtener el indice de la subcadena de Hola:
indice = cadena.find("Hola")
print(f"La subcadena 'Hola' se encuentra en la posición: {indice}")  # Imprime: La subcadena 'Hola' se encuentra en la posición: 0
