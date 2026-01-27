# Identifica la estacion del año

# Se solicita proporcionar el valor de un mes (valor numerico entre 1 y 12), e indicar la estacion del año segun lo siguiente:

# meses 12, 1 o 2 = Verano
# meses 3, 4 o 5 = Otoño
# meses 6, 7 o 8 = Invierno
# meses 9, 10 o 11 = Primavera
# Cualquier otro numero = Mes desconocido

print('=== Identifica la estacion del año ===')

# solicitamos el numero del mes
mes = int(input('Ingrese el numero entero del que corresponde al mes del año (1-12) para saber la estacion: '))

if mes == 1 or mes == 2 or mes == 12:
    print(f'\nEl mes numero {mes} corresponde a la estacion Verano.')
elif mes == 3 or mes == 4 or mes == 5:
    print(f'\nEl mes numero {mes} corresponde a la estacion Otoño.')
elif mes == 6 or mes == 7 or mes == 8:
    print(f'\nEl mes numero {mes} corresponde a la estacion Invierno.')
elif mes == 9 or mes == 10 or mes == 11:
    print(f'\nEl mes numero {mes} corresponde a la estacion Primavera.')
else:
    print(f'\nEl mes numero {mes} no corresponde a ninguna estacion conocida.')

# Fin del programa
print('\n=== Fin del programa ===')