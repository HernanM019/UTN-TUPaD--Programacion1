# ------------------------------------------
# TP UNIDAD 8 - MANEJO DE ARCHIVOS
# ------------------------------------------

# 1. Crear archivo inicial (solo la primera vez)
with open("productos.txt", "w") as archivo:
    archivo.writelines([
        "Lapicera,120.5,30\n",
        "Cuaderno,350.0,15\n",
        "Goma,80.0,50\n"
    ])

# 2. Leer y procesar productos existentes
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        productos.append({
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        })

# Mostrar productos en pantalla
print("\n--- LISTA DE PRODUCTOS ---")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

# 3. Agregar nuevos productos desde teclado
while True:
    agregar = input("\n¿Desea agregar un nuevo producto? (s/n): ").lower()
    if agregar != "s":
        break

    nombre = input("Nombre: ").capitalize()
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    productos.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })

# 4. Buscar producto por nombre
buscar = input("\nIngrese el nombre de un producto para buscar: ").capitalize()
encontrado = False

for p in productos:
    if p["nombre"] == buscar:
        print(f"\nEncontrado → Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("\nEl producto no existe en la lista.")

# 5. Guardar productos actualizados en el archivo
with open("productos.txt", "w") as archivo:
    for p in productos:
        linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
        archivo.write(linea)
        print("\n Archivo actualizado correctamente.")
