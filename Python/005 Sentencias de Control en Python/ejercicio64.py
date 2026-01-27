# Sistema de autenticacion

# Crear un sistema para validar los valores de usuario y password proporcionados.

# Se deben definir dos constantes con los valores validos de usuario y password.

# Y el sistema debe comparar los valores validos contra los valores proporcionados.

# Se deben considerar 4 casos:
    # 1. Usuario y password validos. Debe imprimir "Bienvenido al sistema"
    # 2. Usuario invalido.
    # 3. Password invalido.
    # 4. Usuario y password invalidos.

print('=== Sistema de Autenticacion ===')

# Constantes:
USUARIO = 'admin'
PASSWORD = 'contraseña'

# Solicitamos los datos
usuario = input('''
Usuario: ''')
password = input('''
Password: ''')

# Decoracion
print('-'*30)

# Comparamos
if usuario == USUARIO and password == PASSWORD:
    print('''
Bienvenido al sistema''')
elif not (usuario == USUARIO) and password == PASSWORD:
    print('Error Usuario Invalido')
elif usuario == USUARIO and not(password == PASSWORD):
    print('Error Password Invalido')
else:
    print('Error Usuario y password invalidos')

# Fin del programa
print('\n=== Fin del programa ===')