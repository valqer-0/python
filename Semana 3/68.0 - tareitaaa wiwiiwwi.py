# Productos con sus datos
producto1 = {
    "nombre": "Laptop",
    "precio": 899.99,
    "stock": 5,
    "categoria": "Electrónica"
}

producto2 = {
    "nombre": "Mouse",
    "precio": 25.50,
    "stock": 50,
    "categoria": "Accesorios"
}

producto3 = {
    "nombre": "Teclado",
    "precio": 75.99,
    "stock": 30,
    "categoria": "Accesorios"
}

# Calcular valor total de cada producto
valor_total_p1 = producto1["precio"] * producto1["stock"]
valor_total_p2 = producto2["precio"] * producto2["stock"]
valor_total_p3 = producto3["precio"] * producto3["stock"]

# Calcular valor total del inventario
valor_total_inventario = valor_total_p1 + valor_total_p2 + valor_total_p3

# Mostrar información
print("=== CATÁLOGO DE PRODUCTOS ===\n")

print(f"Producto: {producto1['nombre']}")
print(f"Precio: ${producto1['precio']:.2f} | Stock: {producto1['stock']} | Categoría: {producto1['categoria']}")
print(f"Valor Total: ${valor_total_p1:.2f}\n")

print(f"Producto: {producto2['nombre']}")
print(f"Precio: ${producto2['precio']:.2f} | Stock: {producto2['stock']} | Categoría: {producto2['categoria']}")
print(f"Valor Total: ${valor_total_p2:.2f}\n")

print(f"Producto: {producto3['nombre']}")
print(f"Precio: ${producto3['precio']:.2f} | Stock: {producto3['stock']} | Categoría: {producto3['categoria']}")
print(f"Valor Total: ${valor_total_p3:.2f}\n")

print(f"VALOR TOTAL DEL INVENTARIO: ${valor_total_inventario:.2f}")