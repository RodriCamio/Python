# Casa de los espejos}

# Supon que estas en un parque de diversiones y quieres entrar a la casa de los espejos.

# Sin embargo debes cumplor con algunas condiciones
# 1. Debes tener mas de 10 años.
# 2. No debe darte miedo la oscuridad.

# Si se cumplen las condiciones anteriores puedes entrar.

# Para realizar este ejemplo vamos a utilizar el operador not para aplicar una logica inversa. 

print('=== Casa de los espejos ===')

# Constantes
LIMITE_EDAD = 10
TIENE_MIEDO = 'no'

# Solicitamos los datos
edad = int(input('Indique su edad: '))
miedo = input('Tiene miedo a la oscuridad si/no: ')

if not(edad >= LIMITE_EDAD and miedo.strip().lower() == TIENE_MIEDO):
    print('No puede ingresar')
else:
    print('Si Puede ingresar')

