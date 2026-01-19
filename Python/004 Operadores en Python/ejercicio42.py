# Generacion Ticket Venta

# Supongamos que compramos varios articulos en el supermercado y queremos obtener el ticket de venta total incluyendo impuestos.
# El sistema solicitara el precio de cada producto a comprar y el usuario debera indicar su precio ( valor tipo con punto decimal).
# El sistema debe realizar la suma de cada producto, calcular el impiesto y finalmente imprimir el total de la compra.

print("=== Sistema Generacion de ticket de venta ===")

producto1 = float(input('Precio del primer producto: $'))   # Ingresamos los precios de los productos
producto2 = float(input('Precio del segundo producto: $'))  # Ingresamos los precios de los productos
producto3 = float(input('Precio del tercer producto: $'))   # Ingresamos los precios de los productos

subtotal = producto1 + producto2 + producto3      # Suma de los tres productos

IMPUESTO = (subtotal * 0.21) / 100      # Aca sacamos el 0.21 por ciento del producto que seria el IVA. 

precio_final = subtotal + IMPUESTO # Sumamos el impuesto.
print(f'-'*30 + '\n=== Ticket de venta ===')

print(f'''
Producto 1: ${producto1:.2f}
Producto 2: ${producto2:.2f}
Producto 3: ${producto3:.2f}

Subtotal: ${subtotal:.2f}
Impuesto (0.21%): ${IMPUESTO:.2f}
Total con impuestos: ${precio_final:.2f}

Gracias por su compra!''')