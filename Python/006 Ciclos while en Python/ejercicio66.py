# Ejemplo de ciclos while

# Imprimimos horizontal
contador = 1
while contador <= 5:
    print(contador, end=' ') # el parametro end= nos permite modificar como se va a comportar al final de lo que mandamos a imprimir.
    contador += 1

# Imprimimos vertical separado por una linea
print('\n'+'-'*30)
contador = 1
while contador <= 5:
    print(contador, end='\n'+('-'*5)+'\n') # agregamos una linea entre numero y numero
    contador += 1