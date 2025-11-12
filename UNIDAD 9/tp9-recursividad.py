# ------------------------------------------
# TP7 – RECURSIVIDAD
# ------------------------------------------

# 1) Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# 2) Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# 3) Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


# 4) Decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)


# 5) Verificar palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])


# 6) Suma de dígitos
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)


# 7) Contar bloques en una pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)


# 8) Contar cuántas veces aparece un dígito
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)


# ------------------------------------------
# MENÚ PRINCIPAL
# ------------------------------------------

def menu():
    while True:
        print("\n===== MENÚ PRINCIPAL - TP9: RECURSIVIDAD =====")
        print("1. Factorial de un número")
        print("2. Serie de Fibonacci")
        print("3. Potencia recursiva")
        print("4. Conversión decimal a binario")
        print("5. Verificar si una palabra es palíndromo")
        print("6. Suma de los dígitos de un número")
        print("7. Contar bloques de una pirámide")
        print("8. Contar cuántas veces aparece un dígito")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                num = int(input("Ingrese un número: "))
                for i in range(1, num + 1):
                    print(f"Factorial de {i} = {factorial(i)}")

            case "2":
                num = int(input("Ingrese la cantidad de términos: "))
                print("Serie de Fibonacci:")
                for i in range(num):
                    print(fibonacci(i), end=" ")
                print()

            case "3":
                base = int(input("Base: "))
                exp = int(input("Exponente: "))
                print(f"{base}^{exp} = {potencia(base, exp)}")

            case "4":
                num = int(input("Ingrese un número decimal: "))
                binario = decimal_a_binario(num)
                print(f"El número {num} en binario es {binario if binario != '' else '0'}")

            case "5":
                palabra = input("Ingrese una palabra: ").lower()
                print("Es palíndromo" if es_palindromo(palabra) else "No es palíndromo")

            case "6":
                num = int(input("Ingrese un número: "))
                print(f"La suma de sus dígitos es {suma_digitos(num)}")

            case "7":
                niveles = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))
                print(f"Total de bloques necesarios: {contar_bloques(niveles)}")

            case "8":
                num = int(input("Ingrese un número: "))
                dig = int(input("Ingrese el dígito a buscar: "))
                print(f"El dígito {dig} aparece {contar_digito(num, dig)} veces.")

            case "9":
                print("\n Saliendo del programa...")
                break

            case _:
                print("Opción inválida. Intente nuevamente.")


# --- Ejecución principal ---
menu()
