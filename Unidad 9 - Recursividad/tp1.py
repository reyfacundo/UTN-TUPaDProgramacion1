# 1) Crea una función recursiva que calcule el factorial de un número.
# Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario
def factorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:
        return n * factorial(n - 1)  # Llamada recursiva

num_factorial = int(input("Ingrese un número para calcular factoriales: "))
print("Factoriales:")
for i in range(1, num_factorial + 1):
    print(f"{i}! = {factorial(i)}")

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada.
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

pos_fibo = int(input("Ingrese la posición hasta donde quiere la serie Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(pos_fibo):
    print(fibonacci(i), end=" ")
print()

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente,
# utilizando la fórmula n^m = n * n^(m-1). Prueba esta función en un algoritmo general.
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

b = int(input("Ingrese la base para la potencia: "))
e = int(input("Ingrese el exponente: "))
print(f"{b}^{e} = {potencia(b, e)}")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal
# y devuelva su representación en binario como una cadena de texto.
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero_binario = int(input("Ingrese un número decimal para convertir a binario: "))
binario = decimal_a_binario(numero_binario)
print("Binario:", binario if binario else "0")

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes,
# y devuelva True si es un palíndromo o False si no lo es.
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

pal = input("Ingrese una palabra para verificar si es palíndromo: ").lower()
print("Es palíndromo?", es_palindromo(pal))

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo
# y devuelva la suma de todos sus dígitos.
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)

num_suma = int(input("Ingrese un número para sumar sus dígitos: "))
print("Suma de dígitos:", suma_digitos(num_suma))

# 7) Un niño está construyendo una pirámide con bloques.
# En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo
# y devuelva el total de bloques que necesita para construir toda la pirámide.
def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n - 1)

nivel = int(input("Ingrese el número de bloques del nivel más bajo: "))
print("Total de bloques:", contar_bloques(nivel))

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero)
# y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

num_cd = int(input("Ingrese un número para contar dígitos: "))
dig = int(input("Ingrese el dígito a buscar: "))
print(f"El dígito {dig} aparece {contar_digito(num_cd, dig)} veces")
