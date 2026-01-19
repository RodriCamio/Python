# Sistema Prestamo de libros

# Se pide crear un sistema para una biblioteca, la cual desea prestar libros si cumple con cualquiera de las siguientes condiciones

# 1. El usuario tiene credencial de estudiante
# 2. El usuario vive a no mas de 3 km a la redonda

# Si cumple con cualquiera de estas condiciones se le puede prestar el libro

print("=== Sistema Prestamo de libros ===")
LIMITE_DISTANCIA = 3 # Definimos una constante que es el limite de km hasta donde se puede prestar el libro.
tiene_membresia = input('¿Usted cuenta con la credencial de la biblioteca? (si/no): ') # Consultamos si el usuario tiene credencial.
cantidad_kilometros = int(input('¿A cuantos km a la redonda vives?: ')) # Consultamos al usuario a cuantos kilometros a la redonda vive.

prestamo_libro = (tiene_membresia.strip().lower() == 'si') or (cantidad_kilometros <= LIMITE_DISTANCIA) # Usamos el operador OR para comparar los valores y determinar si alguno de los dos es verdadero o si ninguno lo es. 

print(f'¿Tienes acceso al descuento VIP?: {prestamo_libro}')