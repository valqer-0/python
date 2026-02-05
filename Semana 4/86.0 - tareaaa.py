# ...existing code...
productos = {
    1: {"nombre":"Hamburguesa", "precio":65.00, "stock":20, "categoria":"Comida"},
    2: {"nombre":"Papas fritas", "precio":25.00, "stock":30, "categoria":"Comida"},
    3: {"nombre":"Refresco", "precio":15.00, "stock":50, "categoria":"Bebida"},
    4: {"nombre":"Ensalada", "precio":45.00, "stock":10, "categoria":"Comida"},
    5: {"nombre":"Café", "precio":20.00, "stock":25, "categoria":"Bebida"},
}

def mostrar_menu():
    print("\n=== MENÚ ===")
    for pid, p in productos.items():
        print(f"{pid}. {p['nombre']} - Q{p['precio']:.2f} (stock: {p['stock']})")
    print("0. Finalizar pedido")

def pedir_pedido():
    carrito = {}
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Elige el ID del producto (0 para terminar): "))
        except ValueError:
            print("Entrada inválida, intenta de nuevo.")
            continue
        if opcion == 0:
            break
        if opcion not in productos:
            print("Producto no existe.")
            continue
        try:
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("Cantidad inválida.")
            continue
        if cantidad <= 0:
            print("Ingresa una cantidad mayor a 0.")
            continue
        if cantidad > productos[opcion]["stock"]:
            print("No hay suficiente stock.")
            continue
        carrito[opcion] = carrito.get(opcion, 0) + cantidad
        print(f"Agregado {cantidad} x {productos[opcion]['nombre']}")
    return carrito

def calcular_totales(carrito):
    resumen = []
    subtotal = 0.0
    descuento_por_producto = 0.0
    for pid, qty in carrito.items():
        p = productos[pid]
        total_item = p["precio"] * qty
        # Descuento por compra en cantidad (ej.: 10% si compra 3 o más del mismo producto)
        disc_item = 0.0
        if qty >= 3:
            disc_item = total_item * 0.10
            total_item -= disc_item
        resumen.append((p["nombre"], qty, p["precio"], disc_item, total_item))
        subtotal += total_item
        descuento_por_producto += disc_item
    # Descuento por total de compra
    descuento_por_total = 0.0
    if subtotal >= 300:
        descuento_por_total = subtotal * 0.05
        subtotal -= descuento_por_total
    return resumen, subtotal, descuento_por_producto, descuento_por_total

def elegir_pago(total):
    print("\nFormas de pago disponibles:")
    print("1. efectivo (5% descuento)")
    print("2. tarjeta (3% recargo)")
    print("3. transferencia (sin recargo)")
    while True:
        metodo = input("Elige (efectivo/tarjeta/transferencia): ").strip().lower()
        if metodo in ("efectivo","tarjeta","transferencia"):
            break
        print("Método inválido, intenta de nuevo.")
    recargo = 0.0
    descuento_pago = 0.0
    if metodo == "efectivo":
        descuento_pago = total * 0.05
        total -= descuento_pago
    elif metodo == "tarjeta":
        recargo = total * 0.03
        total += recargo
    # transferencia: sin cambio
    return metodo, total, descuento_pago, recargo

def imprimir_factura(resumen, subtotal, desc_prod, desc_total, metodo_pago, total_final, desc_pago, recargo):
    print("\n=== FACTURA ===")
    for nombre, qty, precio, desc_item, total_item in resumen:
        line_desc = f"(-Q{desc_item:.2f})" if desc_item>0 else ""
        print(f"{qty} x {nombre} @ Q{precio:.2f} => Q{total_item:.2f} {line_desc}")
    print(f"\nSubtotal (con descuentos aplicados): Q{subtotal:.2f}")
    if desc_prod>0:
        print(f"Descuentos por cantidad: Q{desc_prod:.2f}")
    if desc_total>0:
        print(f"Descuento por monto total: Q{desc_total:.2f}")
    if desc_pago>0:
        print(f"Descuento por pago en efectivo: Q{desc_pago:.2f}")
    if recargo>0:
        print(f"Recargo por tarjeta: Q{recargo:.2f}")
    print(f"Método de pago: {metodo_pago}")
    print(f"Total a pagar: Q{total_final:.2f}")

def main():
    print("Bienvenido al Menu Digital Interactivo")
    carrito = pedir_pedido()
    if not carrito:
        print("No se realizó ningún pedido. Saliendo.")
        return
    resumen, subtotal, desc_prod, desc_total = calcular_totales(carrito)
    metodo, total_con_pago, desc_pago, recargo = elegir_pago(subtotal)
    imprimir_factura(resumen, subtotal, desc_prod, desc_total, metodo, total_con_pago, desc_pago, recargo)
    print("\nGracias por su compra!")

if __name__ == "__main__":
    main()
# ...existing code...