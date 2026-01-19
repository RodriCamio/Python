# Generacion Ticket Venta con descuento

# Supongamos que compramos varios articulos en el supermercado y queremos obtener el ticket de venta total incluyendo impuestos y ademas le queremos dar la opcion de agregar un descuento al usuario.
# El sistema solicitara el precio de cada producto a comprar y el usuario debera indicar su precio ( valor tipo con punto decimal).
# El sistema debe realizar la suma de cada producto, calcular el impiesto y finalmente imprimir el total de la compra.

print("=== Sistema Generacion de ticket de venta con descuento ===")

producto1 = float(input('Precio del primer producto: $'))   # Ingresamos los precios de los productos
producto2 = float(input('Precio del segundo producto: $'))  # Ingresamos los precios de los productos
producto3 = float(input('Precio del tercer producto: $'))   # Ingresamos los precios de los productos
producto4 = float(input('Precio del ultimo producto: $'))   # Ingresamos los precios de los productos

subtotal = producto1 + producto2 + producto3 + producto4    # Suma de los tres productos
DESCUENTO = int(input('Quiere agregar un descuento?: ')) # Consultamos si quiere agregar un descuento
DESCUENTO = subtotal * DESCUENTO / 100
subtotal_con_descuento = subtotal - DESCUENTO 
IMPUESTO = subtotal_con_descuento * 0.21       # Aca sacamos el 0.21 por ciento del producto que seria el IVA. 
precio_final = subtotal_con_descuento + IMPUESTO # Sumamos el impuesto.
print(f'-'*30 + '\n=== Ticket de venta ===')

print(f'''
Producto 1: ${producto1:.2f}
Producto 2: ${producto2:.2f}
Producto 3: ${producto3:.2f}
Producto 4: ${producto4:.2f}

Subtotal: ${subtotal:.2f}
Descuento: ${DESCUENTO:.2f}
Subtotal con descuento: $ {subtotal_con_descuento} (10%)
Impuesto (0.21%): ${IMPUESTO:.2f}
Total con impuestos: ${precio_final:.2f}

Gracias por su compra!''')