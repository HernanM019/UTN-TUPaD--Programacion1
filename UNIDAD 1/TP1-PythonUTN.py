from cgi import print_form

#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola mundo")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla

name = input("Inserte su nombre: ")
print(f"Hola {name}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

radio = float(input("Introduce el radio del círculo: "))

# Valor aproximado de pi
pi = 3.14

# Calcular área y perímetro
area = pi * radio**2
perimetro = 2 * pi * radio

# Mostrar resultados
print("Área del círculo:", area)
print("Perímetro del círculo:", perimetro)

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

numero = int(input("Ingresa una cantidad de segundos: "))
hora = numero / 3600
print(f"{numero} segundos son {hora:.2f} horas.")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.
numero = int(input("Introduce un número: "))

print("Tabla de multiplicar del", numero)
print(numero, "x 1 =", numero * 1)
print(numero, "x 2 =", numero * 2)
print(numero, "x 3 =", numero * 3)
print(numero, "x 4 =", numero * 4)
print(numero, "x 5 =", numero * 5)
print(numero, "x 6 =", numero * 6)
print(numero, "x 7 =", numero * 7)
print(numero, "x 8 =", numero * 8)
print(numero, "x 9 =", numero * 9)
print(numero, "x 10 =", numero * 10)

#Idealmente aqui seria conveniente usar un ciclo for, pero siendo que esto es estrictamente con estructuras secuenciales
#no lo apliqué aqui.

#7) # Pedir dos números enteros distintos de 0
a = int(input("Introduce el primer número entero (≠ 0): "))
b = int(input("Introduce el segundo número entero (≠ 0): "))

# Operaciones
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b  # no hay riesgo de dividir entre cero porque pedimos números ≠ 0

# Mostrar resultados
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

#Esto es un escenario ideal donde se asume que el usuario insertará los valores requeridos, no hemos validado que efectivamente
#coloque numeros distintos a cero.

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal.

# Pedir al usuario su peso en kg y altura en metros
peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))

# Calcular IMC
imc = peso / (altura ** 2)

# Mostrar resultado
print("Tu índice de masa corporal es:", imc)

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit.

# Pedir al usuario la temperatura en grados Celsius
celsius = float(input("Introduce la temperatura en grados Celsius: "))

# Conversión a Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Mostrar resultado
print("La temperatura en Fahrenheit es:", fahrenheit)

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

num1 = int(input("Ingrese el 1er numero: "))
num2 = int(input("Ingrese el 2er numero: "))
num3 = int(input("Ingrese el 3er numero: "))

print("El promedio es: ", (num1 + num2 + num3) / 3)