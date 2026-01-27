# Tienda en Linea

# Crear un sistema que ofrezca descuentos dependiendo del monto de la compra, o si es miembro de la tienda.

# Se deben revisar las siguientes condiciones:
# 1. Si ha comprado mas de $1.000,00 y es miembro -> Descuento de 10%
# 2. Si es miembro -> Descuento de 5%
# 3. Si no ha comprado mas de $1.000,00 y no es miembro -> Descuento de 0%

print('=== Tienda en linea ===')

# Constantes
VALOR_MINIMO = 1000 # monto minimo para el descuento
DESCUENTO_MAYOR = 10
DESCUENTO_MINIMO = 5

valor_compra = int(input('Ingrese un el monto de su compra: '))
es_miembro = input('Es miembro de la tienda? (si/no): ')

if valor_compra >= VALOR_MINIMO and es_miembro.lower() == 'si':
    descuento = valor_compra * (DESCUENTO_MAYOR / 100)
    valor_final = valor_compra - descuento
    print(f'${valor_compra} es mayor o igual a ${VALOR_MINIMO} y ademas es miembro de la tienda')
    print(f'Por lo que accede al descuento de {DESCUENTO_MAYOR}% que es de: ${descuento}.')
    print(f'Valor total de la compra: {valor_final}')
elif valor_compra < VALOR_MINIMO and es_miembro.lower() == 'si':
    descuento = valor_compra * (DESCUENTO_MINIMO / 100)
    valor_final = valor_compra - descuento
    print(f'${valor_compra} es menor a ${VALOR_MINIMO} pero es miembro')
    print(f'Por lo que accede al descuento de {DESCUENTO_MINIMO}% que es de: ${descuento}.')
    print(f'Valor total de la compra: {valor_final}')
else:
    print(f'${valor_compra} es menor a ${VALOR_MINIMO} y ademas no es miembro de la tienda')
    print(f'Por lo que no accede a ningun descuento.')
    print(f'Valor total de la compra: {valor_compra}')