# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for num in range(100 + 1):
    print(num)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

num = int(input("Ingrese un número entero: "))

digitos = 0

while num > 0:
    num = num // 10
    digitos += 1

print("Ingrese un número válido")


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

inicio = int(input("Ingrese un número entero: "))
fin = int(input("Ingrese otro número entero: "))

for num in range(inicio+1, fin):
    print(num)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

num = int(input("Ingrese un número entero para sumar. Ingrese un 0 para mostrar el total. "))
total = 0

while num != 0:
    total += num
    num = int(input("Ingrese un número entero para sumar. Ingrese un 0 para mostrar el total. "))

print(f'El total es {total}')


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

num = random.randint(0, 9)
guess = int(input("Ingrese un número entre 0 y 9:  "))
counter = 1

while guess != num:
    guess = int(input("Incorrecto! Ingrese otro número entre 0 y 9:  "))
    counter += 1

print(f'Correcto! Intentos: {counter}')


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for num in range(100, -1, -2):
    print(num)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario

user_num = int(input('Ingrese un número positivo: '))
total = 0

for num in range(user_num+1):
    total += num

print(total)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

even = 0
odd = 0
negative = 0
positive = 0

for counter in range(100):
    num = int(input('Ingrese un número entero: '))
    if num % 2 == 0:
        even += 1
    else: odd += 1
    if num >= 0:
        positive += 1
    else: negative += 1

print(f'Pares: {even} - Impares: {odd} - Negativos: {negative} - Positivos: {positive}')


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

from statistics import mode, median, mean

total = 0
count = 0

for counter in range(100):
    num = int(input('Ingrese un número entero: '))
    total += num
    count += 1

print(f'La media es: {total/count}')


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = str(int(input('Ingrese un número entero: ')))
num_characters = int(len(num))

new_num = ''

for i in range(num_characters-1, -1, -1):
    new_num += num[i]

print(num, new_num)