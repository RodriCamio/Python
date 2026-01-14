# Error comun en booleanos

respuesta = "False" # La variable es una cadena de texto, no un booleano

# La funcion bool evalua si el string no esta vacio, por lo que siempre sera True

es_verdadero = bool(respuesta)
print(es_verdadero)  # Esto imprimira True, lo cual puede ser confuso

# ¿Por que sucede esto? Porque el string "False" no esta vacio, y cualquier string no vacio es considerado True en un contexto booleano.

# Forma correcta de validar vacio:
texto_vacio = ""
print(bool(texto_vacio))  # Esto imprimira False, ya que el string esta vacio

