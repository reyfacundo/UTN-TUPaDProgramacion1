# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

import random
from statistics import mode, median, mean
age = int(input('Ingrese su edad: '))

if age > 18:
    print('Es mayor de edad')

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

grade = int(input('Ingrese su nota: '))

if grade >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par,imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar

evenNumber = int(input('Ingrese un número par: '))

if evenNumber % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
    # ● Niño/a: menor de 12 años.
    # ● Adolescente: mayor o igual que 12 años y menor que 18 años.
    # ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
    # ● Adulto/a: mayor o igual que 30 años.

age = int(input('Ingrese su edad: '))

if age < 12:
    print("Es un niño/a")
elif 12 <= age < 18:
    print("Es un adolescente")
elif 18 <= age < 30:
    print("Es un adulto/a joven")
else:
    print("Es un adulto/a")


# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por enpantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir porpantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el usode la función len() en Python para evaluar la cantidad de elementos que tiene un iterable talcomo una lista o un string.

password = input('Ingrese una contraseña de entre 8 y 14 caracteres: ')

if 8 <= len(password) <= 14:
    print('Ha ingresado una contraseña correcta')
else:
    print('Por favor, ingrese una contraseña de entre 8 y 14 caracteres')


# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente:

    # from statistics import mode, median, mean
    # mi_lista = [1,2,5,5,3]
    # mean(mi_lista)

# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
    # ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.
    # ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda.
    # ● Sin sesgo: cuando la media, la mediana y la moda son iguales.

# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

# Definir la lista numeros_aleatorios de la siguiente forma:

    # import random
    # numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.


numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

meanValue = mean(numeros_aleatorios)
medianValue = median(numeros_aleatorios)
modeValue = mode(numeros_aleatorios)

if ((meanValue > medianValue) and (medianValue > modeValue)):
    print('Sesgo positivo//a la derecha')
elif ((meanValue < medianValue) and (medianValue < modeValue)):
    print('Sesgo negativo//a la izquierda')
else:
    print('Sin sesgo')

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

textInput = input('Ingrese una palabra o frase: ').lower()

lastChar = textInput[-1]

output = textInput + '!' if lastChar == "a" else "b"

if (lastChar == 'a' or lastChar == 'e' or lastChar == 'i' or lastChar == 'o' or lastChar == 'u'):
    print(f'{textInput}!')
else:
    print(textInput)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3dependiendo de la opción que desee:
    # 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
    # 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
    # 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por elusuario e imprimir el resultado por pantalla.
# Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

name = input('Ingrese su nombre: ')
number = int(input('Si quiere su nombre en mayúsculas, ingrese 1. Si quiere su nombre en minúsculas, ingrese 2. Si quiere su nombre con la primera letra en mayúscula, ingrese 3.'))

if number == 1:
    print(name.upper())
elif number == 2:
    print(name.lower())
elif number == 3:
    print(name.title())
else:
    print('No es un número válido!')

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:

    # ● Menor que 3: "Muy leve" (imperceptible).
    # ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
    # ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
    # ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
    # ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
    # ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitude = float(input("Ingrese la magnitud del terremoto: "))

if magnitude < 3:
    print('Muy leve')
elif 3 <= magnitude < 4:
    print('Leve')
elif 4 <= magnitude < 5:
    print('Moderado')
elif 5 <= magnitude < 6:
    print('Fuerte')
elif 6 <= magnitude < 7:
    print('Muy fuerte')
else:
    print('Extremo')


# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año

"""
| Periodo del año  | Estación en el hemisferio norte | Estación en el hemisferio sur |
|------------------|---------------------------------|------------------------------|
| Desde el 21 de diciembre hasta el 20 de marzo (incluidos) | Invierno | Verano |
| Desde el 21 de marzo hasta el 20 de junio (incluidos)     | Primavera| Otoño |
| Desde el 21 de junio hasta el 20 de septiembre (incluidos)| Verano   | Invierno |
| Desde el 21 de septiembre hasta el 20 de diciembre(incluidos)| Otoño | Primavera |
"""

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.


hemisphere = input('Se encuentra en el norte o en el sur? (N o S)').lower()
month = input('Qué mes es? ').lower()
day = int(input('Qué día (número) es?'))

if (((month == "diciembre") and (day >= 21)) or ((month == "marzo") and (day <= 20))):
    print('Invierno')if hemisphere == 'n' else print('Verano')
elif (((month == "marzo") and (day >= 21)) or ((month == "junio") and (day <= 20))):
    print('Primavera')if hemisphere == 'n' else print('Otoño')
elif (((month == "junio") and (day >= 21)) or ((month == "septiembre") and (day <= 20))):
    print('Verano')if hemisphere == 'n' else print('Invierno')
elif (((month == "septiembre") and (day >= 21)) or ((month == "diciembre") and (day <= 20))):
    print('Otoño')if hemisphere == 'n' else print('Primavera')
