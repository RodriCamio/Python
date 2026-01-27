# Valor Positivo

# Un programa que solicite un numero al usuario y determine si es positivo o negativo

# Solicitamos un numero
print('=== Valor Positivo o Negativo ===')
numero = int(input('Ingrese un numero: '))
if numero > 0:
    print(f'{numero} es un numero positivo.')
elif numero == 0:
    print(f'{numero} es cero')
else:
    print(f'{numero} es negativo')