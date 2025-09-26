# Ejercicio 1
i = 0
while i <= 100:
    print(i)
    i = i + 1

# Ejercicio 2
n = int(input("Ingrese un número entero: "))
temp = n
if n == 0:
    digitos = 1
else:
    if n < 0:
        temp = -temp
    digitos = 0
    while temp > 0:
        digitos = digitos + 1
        temp = temp // 10
print("Cantidad de dígitos:", digitos)

# Ejercicio 3
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
if a < b:
    inicio = a + 1
    fin = b
else:
    inicio = b + 1
    fin = a
suma = 0
while inicio < fin:
    suma = suma + inicio
    inicio = inicio + 1
print("Suma:", suma)

# Ejercicio 4
suma = 0
num = int(input("Ingrese un número (0 para terminar): "))
while num != 0:
    suma = suma + num
    num = int(input("Ingrese un número (0 para terminar): "))
print("Total acumulado:", suma)

# Ejercicio 5
import random
objetivo = random.randint(0, 9)
intentos = 0
adivino = False
while not adivino:
    guess = int(input("Adivine el número (0-9): "))
    intentos = intentos + 1
    if guess == objetivo:
        adivino = True
print("Adivinaste. Te tomó ", intentos, " intentos.")

# Ejercicio 6
i = 100
while i >= 0:
    if i % 2 == 0:
        print(i)
    i = i - 1

# Ejercicio 7
n = int(input("Ingrese un número entero positivo: "))
suma = 0
i = 0
while i <= n:
    suma = suma + i
    i = i + 1
print("Suma:", suma)

# Ejercicio 8
pares = 0
impares = 0
positivos = 0
negativos = 0
i = 0
while i < 100:
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    if num > 0:
        positivos = positivos + 1
    elif num < 0:
        negativos = negativos + 1
    i = i + 1
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# Ejercicio 9
suma = 0
i = 0
while i < 100:
    num = int(input("Ingrese un número: "))
    suma = suma + num
    i = i + 1
media = suma / 100
print("Media:", media)

# Ejercicio 10
n = int(input("Ingrese un número para invertir: "))
if n < 0:
    negativo = True
    n = -n
else:
    negativo = False
invertido = 0
while n > 0:
    dig = n % 10
    invertido = invertido * 10 + dig
    n = n // 10
if negativo:
    invertido = -invertido
print("Número invertido:", invertido)

#en todos los ejercicios, he usado int(input. Se asume que siempre se va a colocar un numero o el programa se romperá.