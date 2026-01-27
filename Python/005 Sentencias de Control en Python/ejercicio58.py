# Aplicacion de Salud y Fitness

# Se solicita crear una aplicacion de salud y fitness que solicite lo siguiente:
# - Nombre del usuario.
# - Pasos caminados en el dia.

# Ademas definiremos las siguientes constantes:

META_PASOS_DIARIO = 10000
CALORIAS_POR_PASO = 0.04 # Valor aproximado en kilocalorias.

# Con los valores anteriores debemos calcular las calorias quemadas segun los pasos caminados.
# calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

# Y verificaremos si se cumplio la meta de paoss diarios.
# meta_alcanzada = pasos_diarios >= META_PASOS_DIARIO

print('=== Aplicacion de Salud y Fitness ===')

nombre = input('Ingrese su nombre: ')
pasos_diarios = int(input('Ingrese su cantidad de pasos caminados en el dia: '))

calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO
print(f'Con {pasos_diarios} pasos se quemaron {calorias_quemadas} calorias')

meta_alcanzada = 'Si' if pasos_diarios >= META_PASOS_DIARIO else 'No'
print(f'¿Se cumplio la meta de los {META_PASOS_DIARIO} pasos diario?: \n\n{meta_alcanzada} se cumplio')

print('=== Fin del programa ===')