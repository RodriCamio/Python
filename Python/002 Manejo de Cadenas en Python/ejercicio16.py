# Manejo de Subcadenas (slicing) en Python

texto = "python"

# 1. Basico [inicio:fin]
print(texto[0:4]) # Imprime los primeros cuatro caracteres: "pyth"

# 2. Atajo desde el inicio [:fin]
print(texto[:2])  # Imprime los primeros dos caracteres: "py"

# 3. Atajo hasta el final [inicio:]
print(texto[2:])  # Imprime desde el tercer carácter hasta el final: "thon"

# 4. Uso de índices negativos [-n:]
print(texto[-2:]) # Imprime los últimos dos caracteres: "on"

# 5. Pasos [::paso] (Invertir una cadena)
print(texto[::-1]) # Imprime la cadena invertida: "nohtyp"