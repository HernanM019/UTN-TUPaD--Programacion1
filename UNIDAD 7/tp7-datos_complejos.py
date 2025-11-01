# TP7 - Estructuras de Datos Complejas

# -----------------------------------------------------------
# 1) Diccionario inicial y agregar nuevas frutas
# -----------------------------------------------------------
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Agregar nuevas frutas con precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("\n1) Diccionario actualizado con nuevas frutas:")
print(precios_frutas)

# -----------------------------------------------------------
# 2) Actualizar precios de frutas existentes
# -----------------------------------------------------------
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("\n2) Diccionario con precios actualizados:")
print(precios_frutas)

# -----------------------------------------------------------
# 3) Crear lista con nombres de frutas
# -----------------------------------------------------------
frutas = list(precios_frutas.keys())
print("\n3) Lista de frutas:")
print(frutas)

# -----------------------------------------------------------
# 4) Agenda telefónica
# -----------------------------------------------------------
agenda = {}
print("\n4) Carga de 5 contactos telefónicos:")
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    telefono = input("Ingrese su número telefónico: ")
    agenda[nombre] = telefono

consulta = input("\nIngrese el nombre del contacto a consultar: ")
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("El contacto no existe.")

# -----------------------------------------------------------
# 5) Palabras únicas y conteo de apariciones
# -----------------------------------------------------------
frase = input("\n5) Ingrese una frase: ").lower()

palabras = frase.split()
palabras_unicas = set(palabras)
conteo = {}

for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

print("\nPalabras únicas:", palabras_unicas)
print("Conteo de palabras:", conteo)

# -----------------------------------------------------------
# 6) Promedio de alumnos con tuplas de notas
# -----------------------------------------------------------
alumnos = {}
print("\n6) Ingreso de nombres y notas:")

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Ingrese nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

print("\nPromedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

# -----------------------------------------------------------
# 7) Aprobados en parciales (sets)
# -----------------------------------------------------------
print("\n7) Ejemplo de aprobados en parciales:")
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

print("Aprobaron ambos:", parcial1 & parcial2)
print("Aprobaron solo uno:", parcial1 ^ parcial2)
print("Aprobaron al menos uno:", parcial1 | parcial2)

# -----------------------------------------------------------
# 8) Control de stock con diccionario
# -----------------------------------------------------------
print("\n8) Control de stock:")
stock = {"manzanas": 10, "bananas": 5, "naranjas": 8}

producto = input("Ingrese el nombre del producto: ")

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = int(input("¿Cuántas unidades desea agregar? "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("Producto no encontrado. Ingrese su stock inicial: "))
    stock[producto] = nuevo_stock

print("Stock actualizado:", stock)

# -----------------------------------------------------------
# 9) Agenda de eventos con tuplas como claves
# -----------------------------------------------------------
print("\n9) Agenda de eventos:")
agenda_eventos = {
    ("Lunes", "10:00"): "Reunión de equipo",
    ("Martes", "14:00"): "Clase de Programación",
    ("Viernes", "18:00"): "Gimnasio"
}

dia = input("Ingrese el día: ")
hora = input("Ingrese la hora (HH:MM): ")

actividad = agenda_eventos.get((dia, hora), "No hay actividad programada.")
print(f"Actividad: {actividad}")

# -----------------------------------------------------------
# 10) Invertir claves y valores de un diccionario
# -----------------------------------------------------------
print("\n10) Diccionario invertido de países y capitales:")
paises = {
    "Argentina": "Buenos Aires",
    "Francia": "París",
    "Italia": "Roma",
    "Japón": "Tokio"
}

capitales = {capital: pais for pais, capital in paises.items()}
print(capitales)