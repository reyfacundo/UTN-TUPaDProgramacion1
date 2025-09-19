# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

import random
notas = [3, 7, 1, 9, 4, 10, 8, 6, 5, 2]

print(notas)

max = 0
min = 10
promedio = 0

for i in range(len(notas)):
    if notas[i] > max:
        max = notas[i]
    if notas[i] < min:
        min = notas[i]
    promedio += notas[i]

print(
    f'Promedio: {promedio/len(notas)} - Nota más alta: {max} - Nota más baja: {min} ')

# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

products = []

for i in range(5):
    newProduct = input('Ingrese un producto: ')
    products.append(newProduct)

print(products)

sortedProducts = sorted(products)

eliminar = input('Qué producto desea eliminar?')
products.remove(eliminar)

print(sortedProducts)

# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.


nums = [random.randint(1, 100) for i in range(15)]
even = []
odd = []

for i in range(len(nums)):
    if (nums[i] % 2 == 0):
        even.append(nums[i])
    else:
        odd.append(nums[i])

print(f'Lista: {nums} - Pares: {len(even)} - Impares: {len(odd)}')

# 4) Dada una lista con valores repetidos:

# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.


datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

newList = []

for i in range(len(datos)):
    print(datos[i])
    for n in range(len(newList)):
        print(datos[i], newList[n])
        if datos[i] == newList[n]:
            break
    else:
        newList.append(datos[i])

print(newList)


# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.

# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

estudiantes = ["ana", "lucas", "maria",
                "jorge", "sofia", "pedro", "lucia", "mateo"]

print(estudiantes)

action = input(
    'Quiere agregar un nuevo estudiante o eliminar uno existente?: ')

if action.lower() == "agregar":
    estudiantes.append(input('Ingrese el nombre del nuevo estudiante: '))
elif action.lower() == "eliminar":
    estudiante = input('Ingrese el nombre del estudiante a eliminar: ')
    estudiantes.remove(estudiante)
else:
    print('No es una opción valida.')

print(estudiantes)


# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

lista = [1, 2, 3, 4, 5, 6, 7]
print(lista)
ultimo = lista[-1]
for i in range(len(lista)-1, 0, -1):
    lista[i] = lista[i-1]

lista[0] = ultimo
print(lista)


# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

matriz = [
    [3, 15],
    [8, 13],
    [4, 20],
    [8, 10],
    [13, 16],
    [9, 11],
    [11, 17],
]
dias = ['Lunes', 'Martes', 'Miércoles',
        'Jueves', 'Viernes', 'Sábado', 'Domingo']

promedio_minima = 0
promedio_maxima = 0
amplitud = [0]


for i in range(0, len(matriz)):
    promedio_minima += matriz[i][0]
    promedio_maxima += matriz[i][1]
    if matriz[i][1] - matriz[i][0] > amplitud[0]:
        amplitud = [matriz[i][1] - matriz[i][0], i]

print(
    f'Promedio temp mínima: {promedio_minima // len(matriz)} - Promedio temp máxima: {promedio_maxima // len(matriz)}')

print(
    f'El día con mayor amplitud térmica, con {amplitud[0]}°, fue el: {dias[amplitud[1]]} ')


# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

notas = [
    [3, 5, 8],
    [6, 4, 7],
    [8, 9, 10],
    [3, 5, 2],
    [8, 7, 3],
]

promedio_materia1 = 0
promedio_materia2 = 0
promedio_materia3 = 0

for i in range(0, len(notas)):
    promedio_estudiante = 0
    for n in range(0, len(notas[i])):
        promedio_estudiante += notas[i][n]

    promedio_materia1 += notas[i][0]
    promedio_materia2 += notas[i][1]
    promedio_materia3 += notas[i][2]
    print(f'El promedio del {i+1}° estudiante es: {promedio_estudiante / 3}')

print(
    f'El promedio del la primera, segunda y tercera materia son: {promedio_materia1 / 5}, {promedio_materia2 / 5} y {promedio_materia3 / 5}')


# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

while True:
    for fila in range(3):
        for col in range(3):
            print(tablero[fila][col], end=" ")
        print()
    player1_row = int(input('Jugador 1! [X] Ingrese una fila [1,2,3]'))
    player1_column = int(input('Jugador 1! [X] Ingrese una columna [1,2,3]'))

    tablero[player1_row - 1][player1_column - 1] = 'X'

    for fila in range(3):
        for col in range(3):
            print(tablero[fila][col], end=" ")
        print()

    if input('Quieres seguir jugando? Si - No: ').lower() == "no":
        break

    player2_row = int(input('Jugador 2! [O] Ingrese una fila [1,2,3]'))
    player2_column = int(input('Jugador 2! [O] Ingrese una columna [1,2,3]'))

    tablero[player2_row - 1][player2_column - 1] = 'O'

    if input('Quieres seguir jugando? Si - No: ').lower() == "no":
        break


# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.

ventas = [
    [100, 150, 120, 130, 110, 140, 180],
    [200, 210, 190, 220, 240, 250, 270],
    [300, 330, 310, 350, 360, 380, 390],
    [400, 420, 450, 460, 470, 490, 500]
]
dias = ['Lunes', 'Martes', 'Miércoles',
        'Jueves', 'Viernes', 'Sábado', 'Domingo']

mayor_ventas = [0]
ventas_por_dia = [0,0,0,0,0,0,0]

for i in range(0, len(ventas)):
    total_vendido = 0
    for n in range(0, len(ventas[i])):
        total_vendido += ventas[i][n]
        ventas_por_dia[n] += ventas[i][n]
    if total_vendido > mayor_ventas[0]: mayor_ventas = [total_vendido, i+1]
    print(f'El total vendido del {i+1}° producto es de: {total_vendido}')

print(f'El producto más vendido de fue el {mayor_ventas[1]}°')

mayor_ventas_dia = ventas_por_dia[0]
indice_mayor_dia = 0
for i in range(1, len(ventas_por_dia)):
    if ventas_por_dia[i] > mayor_ventas_dia:
        mayor_ventas_dia = ventas_por_dia[i]
        indice_mayor_dia = i

print(f'El día con mayores ventas totales fue {dias[indice_mayor_dia]} con {mayor_ventas_dia} ventas')
