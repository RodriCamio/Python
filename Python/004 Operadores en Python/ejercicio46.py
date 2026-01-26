# Calculo Area y Perimetro de un Rectangulo

# Se solicita calcular el area y perimetro de un rectangulo aplicando las siguientes formulas.
# area = base * altura
# perimetro = 2 * (base + altura)

print('=== Calculo Area y Perimetro de un Rectangulo ===')

# Ingresemos los valores
BASE = float(input('Ingrese la base: '))
ALTURA = float(input('Ingrese la altura: '))

# Creamos constantes
AREA = BASE * ALTURA
PERIMETRO = 2 * (BASE + ALTURA)

# Imprimimos los resultados
print(f'\nEl Area del rectangulo es: {AREA}. Y el Perimetro es: {PERIMETRO}')