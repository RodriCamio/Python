# Sentencias de Decision

# Las sentencias de decision nos permiten controlar el flujo de ejecucion de un programa
# Las estructuras que podemos usar son: if, else y elif.

# La sentencia IF permite ejecutar un bloque de codigo si la condicion  a evaluar es verdadera. Una condicion es una expresion que evalua a True o False, Ej: edad >= 18

# Sistaxis sentencia if
# if condicion:
    # Bloque de codigo que se ejecuta si la condicion es True

print('Ejemplo de Sentencia If: ')
edad = int(input('Carga tu edad: '))
if edad >= 18:
    print('Eres mayor de edad.')