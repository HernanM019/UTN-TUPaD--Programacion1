# -------------------------------------------------------------
# TP6 - FUNCIONES - PROGRAMACIÓN I (UTN)
# -------------------------------------------------------------

import math

# 1. Imprimir "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Saludo personalizado
def saludar_usuario(nombre):
    return "Hola " + nombre + "!"

# 3. Información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print("Soy", nombre, apellido, "tengo", edad, "años y vivo en", residencia)

# 4. Área y perímetro de un círculo
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 5. Convertir segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Tabla de multiplicar
def tabla_multiplicar(numero):
    print("\nTabla de multiplicar del", numero)
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

# 7. Operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    producto = a * b
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero"
    return suma, resta, producto, division

# 8. Cálculo del IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)

# 9. Conversión Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 10. Promedio de tres números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3


# -------------------------------------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------------------------------------
if __name__ == "__main__":
    imprimir_hola_mundo()

    nombre = input("\nIngrese su nombre: ")
    print(saludar_usuario(nombre))

    print("\n--- Información Personal ---")
    nom = input("Nombre: ")
    ape = input("Apellido: ")
    edad = input("Edad: ")
    residencia = input("Residencia: ")
    informacion_personal(nom, ape, edad, residencia)

    print("\n--- Círculo ---")
    radio = float(input("Ingrese el radio: "))
    print("Área:", calcular_area_circulo(radio))
    print("Perímetro:", calcular_perimetro_circulo(radio))

    segundos = int(input("\nIngrese una cantidad de segundos: "))
    print("Equivalen a", segundos_a_horas(segundos), "horas")

    numero = int(input("\nIngrese un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)

    print("\n--- Operaciones Básicas ---")
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    resultados = operaciones_basicas(a, b)
    print("Suma:", resultados[0])
    print("Resta:", resultados[1])
    print("Multiplicación:", resultados[2])
    print("División:", resultados[3])

    print("\n--- IMC ---")
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en metros: "))
    print("Tu IMC es", calcular_imc(peso, altura))

    print("\n--- Conversión de Temperatura ---")
    celsius = float(input("Ingrese la temperatura en °C: "))
    print(celsius, "°C equivalen a", celsius_a_fahrenheit(celsius), "°F")

    print("\n--- Promedio ---")
    n1 = float(input("Primer número: "))
    n2 = float(input("Segundo número: "))
    n3 = float(input("Tercer número: "))
    print("El promedio es", calcular_promedio(n1, n2, n3))

    print("\n--- Fin del programa ---")
