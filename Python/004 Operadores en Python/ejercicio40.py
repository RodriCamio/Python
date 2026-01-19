# Operador NOT
# 
# # El operador NOT invierte el valor del operando.

# Tabla de verdad NOT
print(f'-'*30 + '\n=== Tabla de verdad NOT ===\n')
from tabulate import tabulate

tabla = [
    [False, True],
    [True,  False],
]

encabezados = ["a", "NOT a"]

print(tabulate(tabla, headers=encabezados, tablefmt="grid"))