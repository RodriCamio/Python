# Operadores Logicos

# Los operadores logicos se utilizan para realizar opraciones logicas con valores booleanos.

# Operador Logico and (y): Devuelve True si ambos operadores son verdaderos.
# Sintaxis operador Logico:
# exp1 and exp2
# Ejemplo:
exp1 = False
exp2 = True
print(f'-'*30 + '\n=== Operador Logico AND ===\n')
print(f'False and True: {exp1 and exp2}') # False
print(f'True and True: {exp2 and exp2}') # True
print(f'False and False: {exp1 and exp1}') # False

# Operador Logico or (o): Devuelve True si cualquiera de los operadores son verdaderos.
# Sintaxis operador Logico:
# exp1 or exp2
# Ejemplo:
print(f'-'*30 + '\n=== Operador Logico OR ===\n')
print(f'False or True: {exp1 or exp2}') # True
print(f'True or True: {exp2 or exp2}') # True
print(f'False or False: {exp1 or exp1}') # False 

# Operador Logico not (no): Invierte  el valor del operado. Es un operador unario
# Sintaxis operador Logico:
# not exp1
# Ejemplo:
print(f'-'*30 + '\n=== Operador Logico NOT ===\n')
print(f'Not True: {not exp2}') # False
print(f'Not False: {not exp1}') # True