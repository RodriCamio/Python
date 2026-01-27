# Sistema de calificaciones

# Crear un programa para convertir una calificacion numerica (entre 0 y 10) a una letra ( de la F a la A).

# si es mayor o igual a 9 y menor o igual a 10 es una A
# si es mayor o igual a 8 y menor a 9 es una B
# si es mayor o igual a 7 y menor a 8 es una C
# si es mayor o igual a 6 y menor a 7 es una D
# si es mayor o igual a 0 y menor a 6 es una F

# En otro caso imprimir "Valor desconocido".

print('=== Sistema de calificaciones ===')

calificacion_num = float(input('Ingrese la calificacion numerica: '))

if 9 <= calificacion_num <= 10:
    print(f'La calificacion {calificacion_num} significa que es una A')
elif 8 <= calificacion_num < 9:
    print(f'La calificacion {calificacion_num} significa que es una B')
elif 7 <= calificacion_num < 8:
    print(f'La calificacion {calificacion_num} significa que es una C')
elif 6 <= calificacion_num < 7:
    print(f'La calificacion {calificacion_num} significa que es una D')
elif 0 <= calificacion_num < 6:
    print(f'La calificacion {calificacion_num} significa que es una F')
else:
    print(f'La calificacion {calificacion_num} es un Valor desconocido')