# Sentencia if elif else

# La sentencia else se usa para ejecutar un bloque de codigo cuando la condicion del if es falsa.

# Sintaxis sentencia if else.
# if condicion 1:
    # Bloque de codigo que se ejecuta
    # si la condicion 1 es verdadera.
# elif condicion 2:
    # Bloque de codigo que se ejecuta
    # si la condicion 2 es verdadera.
# else:
    # Bloque de codigo que se ejecuta
    # si ninguna condicion es verdadera.

# Ejemplo de sentencia if elif else:
print('Ejemplo de Sentencia If Else: ')
edad = int(input('Carga tu edad: '))
if edad >= 18:
    print('Eres un adulto.')
elif 13 <= edad < 18:
    print('Eres un adolescente')
else:
    print('Eres un niño/a.')