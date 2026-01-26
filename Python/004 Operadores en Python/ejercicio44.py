# Sistema de Autenticacion

# Crea un programma ppara validad el usuario y password proporcionados por el usuario.
# Crea 2 constantes con los valores correctos y porteriormente compara que el usuario y password, proporcionados por el usuario sean validos.
# Debe solicitar el usuario y el password al usuario y si son iguales que los valores correctos almacenados en las constantes debe imprimir True, de lo contrario debe imprimir False.

print("=== Sistema de Autenticacion ===")

# Creamos las constantes
USUARIO = 'admin'
PASSWORD = 123

# Solicitamos los datos al usuario:
usuario = input(f'Ingrese el usuario: ')
password = int(input(f'Ingrese el password: '))

# Corroboramos que los datos sean correctos
print(f'Datos correctos? {USUARIO == usuario and PASSWORD == password}')

