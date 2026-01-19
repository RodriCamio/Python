# Operador AND
# El operador and regresa verdadero si ambos operados son verdaderos

# Tabla de verdad AND
print(f'-'*30 + '\n=== Tabla de verdad AND ===\n')
from tabulate import tabulate

tabla = [
    [False, False, False],
    [False, True,  False],
    [True,  False, False],
    [True,  True,  True],
]

encabezados = ["a", "b", "a AND b"]

print(tabulate(tabla, headers=encabezados, tablefmt="grid"))