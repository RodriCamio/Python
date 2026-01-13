# Generador de Email

# Crea un programa para generar una dirección de correo electrónico
# a partir de los siguientes datos:
# Nombre: Juan Perez
# Empresa: OpenAI
# Dominio: com.ar

# Resultado esperado: 
# email: juan.perez@openai.com.ar

print("=== Generador de Email ===")

# Datos de entrada
nombre = "Juan Perez"
empresa = "OpenAI"
dominio = "com.ar"
sangria = " " * 4

print(f"""
Datos proporcionados:
{sangria} Nombre: {nombre}
{sangria} Empresa: {empresa}
{sangria} Dominio: {dominio}
""")
# Procesamiento de los datos
nombre_lower = nombre.lower().replace(" ", ".")
empresa_lower = empresa.lower()
email = f"{nombre_lower}@{empresa_lower}.{dominio}"
# Salida del resultado
print(f"Email generado: {email}")
# Imprime: Email generado: juan.perez@openai.com.ar