# Operador OR

# El operador OR regresa verdadero (True) si cualquiera de los operadors es verdadero.

# Tabla de verdad OR
print(f'-'*30 + '\n=== Tabla de verdad OR ===\n')
from tabulate import tabulate

tabla = [
    [False, False, False],
    [False, True,  True],
    [True,  False, True],
    [True,  True,  True],
]

encabezados = ["a", "b", "a OR b"]

print(tabulate(tabla, headers=encabezados, tablefmt="grid"))