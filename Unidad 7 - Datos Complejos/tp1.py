"""
1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
"""

precios_frutas = {"Banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

"""
2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
"""

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

"""
3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios.
"""

frutas = list(precios_frutas.keys())

"""
4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
"""

agenda = {}

for i in range(5):
    key = input("Ingrese el nombre del contacto: ")
    value = input("Ingrese el número del contacto: ")
    agenda[key] = value

print(agenda)

consulta = input("Nombre de contacto a consultar?: ")

if consulta not in agenda:
    print("Contacto no existente")
else:
    print(consulta, ": ", agenda[consulta])


"""
5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.
"""

frase = input("Ingrese una frase: ").split()

palabras_unicas = set(frase)

recuento = {}

for palabra in frase:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("palabras_unicas: ", palabras_unicas)
print("recuento: ", recuento)


"""
6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.
"""

alumnos = {}

for i in range(3):
    alumno = input("Ingrese el nombre del alumno: ")
    notas = []
    for n in range(3):
        nota = int(input("Ingrese una nota: "))
        notas.append(nota)
    alumnos[alumno] = tuple(notas)


promedio = {}

for alumno in alumnos:
    promedio[alumno] = sum(alumnos[alumno]) / 3


print(alumnos)
print(promedio)


"""
7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
"""


parcial_1 = {1, 2, 3, 5, 6, 7}
parcial_2 = {2, 4, 6, 8}

ambos_aprobados = parcial_1 & parcial_2
uno_aprobado = parcial_1 ^ parcial_2
al_menos_uno = parcial_1 | parcial_2

print("Aprobaron ambos:", ambos_aprobados)
print("Aprobaron solo uno:", uno_aprobado)
print("Aprobaron al menos uno:", al_menos_uno)


"""
8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.
"""

stock = {
    "manzanas": 50,
    "bananas": 30,
    "naranjas": 20,
    "leche": 15,
    "pan": 40,
    "yerba": 25,
}


producto = input("Ingresá el nombre del producto: ").lower()

if producto in stocks:
    print(f"El stock de {producto} es: {stocks[producto]}")

    agregar = int(input("¿Cuántas unidades querés agregar? "))
    stocks[producto] += agregar

    print(f"Stock actualizado de {producto}: {stocks[producto]}")
else:
    print(f"El producto '{producto}' no existe.")

    agregar_nuevo = input("¿Querés agregarlo como nuevo producto? (si/no): ").lower()

    if agregar_nuevo == "si":
        unidades = int(input("Ingresá el stock inicial: "))
        stocks[producto] = unidades
        print(f"Producto '{producto}' agregado con stock: {stocks[producto]}")
    else:
        print("No se agregó el producto.")

print("Estado final del diccionario:")
print(stock)


"""
9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Permití consultar qué actividad hay en cierto día y hora.
"""

agenda = {
    ("lunes", "09:00"): "Reunión con equipo",
    ("lunes", "14:00"): "Clase de Python",
    ("martes", "10:00"): "Cita médica",
    ("miércoles", "16:00"): "Entrenamiento",
}

dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora: ")

evento = agenda.get((dia, hora))

if evento:
    print(f"En {dia} a las {hora}, tenés: {evento}")
else:
    print(f"No hay eventos programados para {dia} a las {hora}.")


"""
10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores.
"""


paises = {"Argentina": "Buenos Aires", "Brasil": "Brasilia", "Chile": "Santiago"}


nuevo_diccionario = {}

for pais in paises:
    nuevo_diccionario[paises[pais]] = pais

print(nuevo_diccionario)
