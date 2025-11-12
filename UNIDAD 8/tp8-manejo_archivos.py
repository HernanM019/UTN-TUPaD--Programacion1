# ------------------------------------------
# TP UNIDAD 8 - MANEJO DE ARCHIVOS
# ------------------------------------------

ARCHIVO = "productos.txt"

# --- Funciones auxiliares ---

def crear_archivo_inicial():
    """Crea el archivo productos.txt con datos base (solo una vez)."""
    with open(ARCHIVO, "w") as archivo:
        archivo.writelines([
            "Lapicera,120.5,30\n",
            "Cuaderno,350.0,15\n",
            "Goma,80.0,50\n"
        ])
    print("\n Archivo inicial creado correctamente.")


def leer_productos():
    """Lee los productos del archivo y devuelve una lista de diccionarios."""
    productos = []
    try:
        with open(ARCHIVO, "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(",")
                productos.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })
    except FileNotFoundError:
        print("\n No se encontró el archivo. Creá uno nuevo desde el menú.")
    return productos


def mostrar_productos(productos):
    """Muestra los productos en pantalla."""
    if not productos:
        print("\nNo hay productos para mostrar.")
        return
    print("\n--- LISTA DE PRODUCTOS ---")
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")


def agregar_producto(productos):
    """Agrega un nuevo producto a la lista."""
    nombre = input("Nombre: ").capitalize()
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    productos.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    print(f"\n Producto '{nombre}' agregado correctamente.")


def buscar_producto(productos):
    """Busca un producto por nombre y lo muestra si existe."""
    nombre = input("Ingrese el nombre del producto a buscar: ").capitalize()
    for p in productos:
        if p["nombre"] == nombre:
            print(f"\nEncontrado → Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
            return
    print("\nProducto no encontrado.")


def guardar_productos(productos):
    """Guarda todos los productos en el archivo (sobrescribe)."""
    with open(ARCHIVO, "w") as archivo:
        for p in productos:
            linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
            archivo.write(linea)
    print("\n💾 Cambios guardados correctamente.")


# --- Programa principal ---

def menu():
    productos = leer_productos()

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Crear archivo inicial")
        print("2. Mostrar productos")
        print("3. Agregar producto")
        print("4. Buscar producto")
        print("5. Guardar cambios")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                crear_archivo_inicial()
                productos = leer_productos()
            case "2":
                mostrar_productos(productos)
            case "3":
                agregar_producto(productos)
            case "4":
                buscar_producto(productos)
            case "5":
                guardar_productos(productos)
            case "6":
                print("\nSaliendo del programa...")
                break
            case _:
                print("\nOpción inválida. Intente nuevamente.")


menu()