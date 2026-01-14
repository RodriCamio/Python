# Sistema Generador de Emails

# Se solicita crear una nueva version del sistema generador de emails.
# Para generar un email se debe solicitar:
# - Nombre
# - Apellido
# - Nombre de la empresa
# - Extension Dominio (Ej: .com, .ar, .org, etc)

# El resultado debe ser:
# Ejemplo: Nombre: Juan, Apellido: Perez, Empresa: Google, Extension Dominio: .com 
# Email Generado: juan.perez@google.com

print("=== Sistema Generador de Emails ===")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
empresa = input("Ingrese el nombre de la empresa: ")
extension_dominio = input("Ingrese la extensión del dominio (ej: .com, .ar, .org, etc): ")

email_generado = f"{nombre.strip().lower().replace(' ', '.')}.{apellido.strip().lower().replace(' ', '.')}@{empresa.strip().lower().replace(' ', '.')}{extension_dominio.strip().lower().replace(' ', '.')}"
print("-"*30)
print(f"Email Generado: {email_generado}")
print("-"*30)
print("Gracias por utilizar el Sistema Generador de Emails.")