producto = {
    "nombre":"Mouse Gamer",
    "precio":85.50,
    "descuento":0.15
}

precio_original = producto.get("precio")
descuento = producto["descuento"]

precio_final = precio_original - precio_original*descuento
print(precio_final)