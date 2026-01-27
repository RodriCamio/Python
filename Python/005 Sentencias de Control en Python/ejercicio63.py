# Sistema de Envios

# Crea un programa para determinar el costo de envio de un paquete segun el destino (nacional o internacional) y el peso del paquete.

# costo tarifa:
    # - Nacional = 10 x kilo
    # - Internacional = 20 x kilo

# El programa debe solicitar 2 valores:
    # 1. Destino (nacional o internacional)
    # 2. Peso (kilogramos) del paquete

# Al final debe imprimir el costo de envio del paquete.

print('=== Sistema de Envios ===')

# Constantes
NACIONAL = 10
INTERNACIONAL = 20

# Solicitar
tipo_de_envio = input(f'''
Ingrese el tipo de destino
    - Nacional = ${NACIONAL} por Kg.
    - Internacional = ${INTERNACIONAL} por Kg.

¿tu envio es de que tipo?: ''')

peso_del_envio = float(input('Ingrese el peso del paquete: '))

# Decoracion
print('-'*30)

# Calculo
if tipo_de_envio.strip().lower() == 'nacional':
    print(f'''
El envio es de tipo: Nacional 
Con un peso de {peso_del_envio}kg

tiene un precio de: ${NACIONAL * peso_del_envio}''')
elif tipo_de_envio.strip().lower() == 'internacional':
    print(f'''
El envio es de tipo: Internacional 
Con un peso de {peso_del_envio}kg

tiene un precio de: ${INTERNACIONAL * peso_del_envio}''')
else:
    print('El valor ingresado no es correcto, tiene que ser "Nacional" o "Internacional".')

# Fin del programa
print('\n=== Fin del programa ===')