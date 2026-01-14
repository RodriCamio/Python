# La funcion boolean() convierte un valor a su equivalente booleano (True o False).

# Las reglas del juego

# Falsy: 
# Representan "nada" o "vacio"
# 0 (cero int/float)
# "" (cadena vacia)
# [] (lista vacia)
# none (Ausencia de valor)

# Truthy:
# Cualquier cosa que "Existe"
# 1 (cero int/float)
# "Hola" (cadena con contenido)
# [1,2,3] (lista con contenido)
# True (Valor booleano verdadero)

# Programa: Funcion bool

# 1. Numero (int y float)
print(bool(0))        # Falsy
print(bool(0.0))      # Falsy
print(bool(42))       # Truthy

# 2. Cadenas de texto (str)
print(bool(""))       # Falsy
print(bool("Hola"))   # Truthy
print(bool(" "))      # Truthy

# 3. None (Ausencia de valor)
print(bool(None))     # Falsy
print(bool(True))     # Truthy
print(bool(False))    # Falsy

