import random

# Ejercicio 1
notas = [7, 8, 10, 5, 6, 9, 4, 7, 8, 6]
print("Notas:", notas)
print("Promedio:", sum(notas) / len(notas))
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))

# Ejercicio 2
productos = []
for i in range(5):
    p = input("Ingrese un producto: ")
    productos.append(p)

print("Productos ordenados:", sorted(productos))

elim = input("Ingrese un producto a eliminar: ")
if elim in productos:
    productos.remove(elim)
print("Lista actualizada:", productos)

# Ejercicio 3
numeros = [random.randint(1, 100) for _ in range(15)]
pares = []
impares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print("Números:", numeros)
print("Cantidad pares:", len(pares))
print("Cantidad impares:", len(impares))

# Ejercicio 4
valores = [1, 2, 2, 3, 4, 4, 5]
sin_repetidos = []
for v in valores:
    if v not in sin_repetidos:
        sin_repetidos.append(v)
print("Original:", valores)
print("Sin repetidos:", sin_repetidos)

# Ejercicio 5
estudiantes = ["Ana", "Luis", "Marta", "Juan", "Sofía", "Pedro", "Elena", "Diego"]
accion = input("¿Quiere agregar (A) o eliminar (E) un estudiante?: ")
if accion.upper() == "A":
    nuevo = input("Ingrese el nombre del estudiante: ")
    estudiantes.append(nuevo)
elif accion.upper() == "E":
    eliminar = input("Ingrese el nombre a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
print("Lista final:", estudiantes)

# Ejercicio 6
numeros = [1, 2, 3, 4, 5, 6, 7]
ultimo = numeros.pop()   # saca el último
numeros.insert(0, ultimo) # lo pone al principio
print("Lista rotada:", numeros)

# Ejercicio 7
temperaturas = [
    [12, 25], [14, 28], [10, 22], [11, 21], [13, 27], [9, 19], [15, 26]
]
suma_min = 0
suma_max = 0
amplitud_max = 0
dia_amplitud = 0
for i in range(len(temperaturas)):
    tmin, tmax = temperaturas[i]
    suma_min += tmin
    suma_max += tmax
    if (tmax - tmin) > amplitud_max:
        amplitud_max = tmax - tmin
        dia_amplitud = i + 1
print("Promedio mínimas:", suma_min / len(temperaturas))
print("Promedio máximas:", suma_max / len(temperaturas))
print("Mayor amplitud térmica en el día:", dia_amplitud)

# Ejercicio 8
notas = [
    [7, 8, 9],
    [6, 5, 7],
    [8, 9, 10],
    [4, 6, 5],
    [9, 9, 8]
]
for i in range(len(notas)):
    print("Promedio estudiante", i+1, ":", sum(notas[i]) / len(notas[i]))
for j in range(3):
    suma = 0
    for i in range(len(notas)):
        suma += notas[i][j]
    print("Promedio materia", j+1, ":", suma / len(notas))

# Ejercicio 9
tablero = [["-","-","-"],["-","-","-"],["-","-","-"]]
for turno in range(2):  # solo dos jugadas de ejemplo
    fila = int(input("Ingrese fila (0-2): "))
    col = int(input("Ingrese columna (0-2): "))
    simbolo = input("Ingrese X o O: ").upper()
    tablero[fila][col] = simbolo
    for fila in tablero:
        print(fila)

# Ejercicio 10
ventas = [
    [10, 12, 9, 15, 14, 11, 13],
    [5, 7, 6, 8, 9, 10, 12],
    [20, 22, 21, 19, 25, 23, 24],
    [8, 9, 7, 6, 10, 11, 12]
]
for i in range(len(ventas)):
    print("Total producto", i+1, ":", sum(ventas[i]))

dia_mayor = 0
ventas_max_dia = 0
for j in range(7):
    suma = 0
    for i in range(4):
        suma += ventas[i][j]
    if suma > ventas_max_dia:
        ventas_max_dia = suma
        dia_mayor = j + 1
print("Día con más ventas totales:", dia_mayor)

totales_productos = [sum(p) for p in ventas]
mas_vendido = max(totales_productos)
print("Producto más vendido es el", totales_productos.index(mas_vendido) + 1)
