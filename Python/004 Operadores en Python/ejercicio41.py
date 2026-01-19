# Fuera de rango - Operador NOT

# Verificar si un numero esta dentro del rango del 1 al 10
dato = int(input('Ingrese un dato entero: '))

# Revisamos si esta dentro del rango:
# dentro_rango = (1 <= dato <= 10) # si el dato es mayor o igual que 1 y menor o igual que 10 va a dar true de lo contrario va a dar false.
# print(f'¿El numero esta dentro del rango del 1 al 10?: {dentro_rango}')

# Invertimos la logica:
fuera_rango = not(1 <= dato <= 10) # si el dato es mayor o igual que 1 y menor o igual que 10 va a dar true de lo contrario va a dar false.
print(f'¿El numero esta fuera del rango del 1 al 10?: {fuera_rango}')