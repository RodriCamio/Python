# Sistema Bancario

# Considernado que estamos dentro de un sistema bancario, se solicita preguntar al usuario si desea continuar desntro del sistema.

# Utilizando el operador not para aplicar una logica inversa se debe programar las siguientes condiciones:
# Si NO deseamos salir del sistema, imprimir:
    # Continuamos dentro del sistema...
# De lo contrario, imprimimos:
    # Saliendo del sistema...

print('=== Sistema bancario ===')

salir = input('Desea salir del sistema? si/no: ')

if not (salir.strip().lower() == 'si'):
    print(f'Continuamos dentro del sistema...')
else:
    print(f'Saliendo del sistema...')