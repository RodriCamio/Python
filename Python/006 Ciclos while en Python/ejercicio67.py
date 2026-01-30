# Calculador de recursos

# Tengo un mapa de google con lineas marcadas de un posible recorrido de los cables para camaras de seguridad. 
# Los cableados se dividen en dos tipos:
    # UTP = n < 100 mts
    # Fibra Optica = 100 mts <= n <= 1000 mts

# El objetivo es crear un programa que me agregue el 20 mts a todos los cableados que sean UTP, sin que pase los el limite de 100 mts, de lo contrario debe clasificarse como fibra optica. 
# Debe Clasificar el cableado y devolver, si es utp o fo y la cantidad de cable necesaria, ejemplo: si paso 60 mts, la cantidad de cable necesaria va a ser 80 mts y como es menor a 100 sigue siendo UTP.

# Titulo 
print('=== Calculadora y clasificadora de cableados ===')

# Solicitamos datos:
distancia_cableado = float(input('Ingrese la cantidad de metros que tiene el cableado: '))

# Constantes
LIMITE = 80 # le pongo un limite de 80 porque cuando le sumemos los 20 metros de cable va a llegar a 100 y debe considerarse como FO. 
UTP = distancia_cableado < LIMITE 
FO = LIMITE <= distancia_cableado
AGREGADO_UTP = 20
AGREGADO_FO = 1.20

# Comparamos
if UTP:
    cableado_necesario = distancia_cableado + AGREGADO_UTP
    print(f'Es UTP y necesita {cableado_necesario} mts de cable CAT6 para realizar el trabajo')
elif FO:
    cableado_necesario = distancia_cableado * AGREGADO_FO
    print(f'Es FO y necesita {cableado_necesario} mts de fibra drop para realizar el trabajo')
else:
    print('El dato ingresado no es correcto')