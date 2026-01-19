# Operador AND
# El operador and regresa verdadero si ambos operados son verdaderos
# // Para realizar esta tabla es necesario instalar tabulate //
# // python pip install tabulate o pip install tabulate si estas en linux y tu terminal te lo permite. 

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