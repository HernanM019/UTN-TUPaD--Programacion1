# 1) Edad mayor a 18
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")


# 2) Nota aprobada o desaprobada
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# 3) Número par
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# 4) Categoría por edad
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")


# 5) Contraseña válida
password = input("Ingrese una contraseña: ")
if 8 <= len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# 6) Media, mediana y moda
import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
else:
    print("Sin sesgo")

#Creo que en una parte de los apuntes se menciona la libreria statistics, pero por las dudas... preparé adicionalmente una version
#"manual" sin el uso de la librería. Fue mucho mas dificil de lo que pensaba.

# Ejercicio 6
import random

# Generamos la lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print("Lista:", numeros_aleatorios)

# ---- Calcular la MEDIA ----
suma = 0
for n in numeros_aleatorios:
    suma += n
media = suma / len(numeros_aleatorios)

# ---- Calcular la MEDIANA ----
# Ordenamos la lista
ordenada = sorted(numeros_aleatorios)
n = len(ordenada)
if n % 2 == 0:  # cantidad par
    mediana = (ordenada[n//2 - 1] + ordenada[n//2]) / 2
else:           # cantidad impar
    mediana = ordenada[n//2]

# ---- Calcular la MODA
max_frecuencia = 0
moda = ordenada[0]

for i in range(n):
    contador = 0
    for j in range(n):
        if ordenada[i] == ordenada[j]:
            contador += 1
    if contador > max_frecuencia:
        max_frecuencia = contador
        moda = ordenada[i]

# ---- Mostrar resultados ----
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

# ---- Determinar el sesgo ----
if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
else:
    print("Sin sesgo")



# 7) String terminado en vocal
texto = input("Ingrese una palabra o frase: ")
if texto[-1].lower() in "aeiou":
    print(texto + "!")
else:
    print(texto)


# 8) Transformación de nombre
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 para mayúsculas, 2 para minúsculas, 3 para inicial mayúscula: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")


# 9) Magnitud del terremoto
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")


# 10) Estaciones del año según nuestro hemisferio
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día: "))
hemisferio = input("Ingrese su hemisferio (N/S): ").upper()

if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
    estacionN, estacionS = "Invierno", "Verano"
elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
    estacionN, estacionS = "Primavera", "Otoño"
elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
    estacionN, estacionS = "Verano", "Invierno"
else:
    estacionN, estacionS = "Otoño", "Primavera"

if hemisferio == "N":
    print("Estación:", estacionN)
else:
    print("Estación:", estacionS)
