# Sistema Reserva Hotel

# Se solicita crear un sistema de Reservacion de un hotel.
# Se debe pedir la siguiente informacion al usuario. 

# - Nombre de Cliente
# - Dias de estadia en el hotel?
# - Cuarto con vista al mar?

# El Hotel tiene las siguientes tarifas:

# - Cuarto sin vista al mar $ 150,50 por dia
# - Cuarto con vista al mar $ 190,50 por dia

# El sistema debe calcuclar el costo total de la estadia dependiendo si escogio un cuarto con vista al mar o no.
# Ademas  de indicar si escogio un cuarto con vista al mar o no.

print('=== Sistema Reserva Hotel ===')

# Constantes:
CUARTO_VISTA_AL_MAR = 190.50
CUARTO_SIN_VISTA_AL_MAR = 150.50

# Solicitamos los datos:
nombre = input('Ingrese su nombre de cliente: ')
dias_estadia = int(input('Ingrese cuantos dias de estadia quieren reservar: '))
cuarto = input('Ingrese si quiere vista al mar o no (si/no): ')

# imprimimos la eleccion del cuarto
if cuarto == 'si':
    print(f'Usted eligio el cuarto con vista al mar que tiene un costo de ${CUARTO_VISTA_AL_MAR}')
else:
    print(f'Usted eligio el cuarto sin vista al mar que tiene un costo de ${CUARTO_SIN_VISTA_AL_MAR}')


# Calculamos el costo por dia
valor_cuarto = CUARTO_VISTA_AL_MAR if cuarto.strip().lower() == 'si' else CUARTO_SIN_VISTA_AL_MAR
costo = valor_cuarto * dias_estadia

print(f'El costo total por {dias_estadia} dias de estadia es de: ${costo}')

# Fin
print('=== Fin del programa ===')