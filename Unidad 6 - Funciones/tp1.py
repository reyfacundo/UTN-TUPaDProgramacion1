'''
1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.
'''
def imprimir_hola_mundo():
    return 'Hola Mundo!'

print(imprimir_hola_mundo())


'''
2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.
'''
def saludar_usuario(nombre):
    return f'Hola {nombre}!'

nombre = input('Ingrese su nombre: ')
print(saludar_usuario(nombre))


'''
3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
'''

def informacion_personal(nombre,apellido, edad, residencia):
    return f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}'

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = input('Ingrese su edad: ')
residencia = input('Ingrese su residencia: ')
print(informacion_personal(nombre,apellido,edad,residencia))


'''
4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
'''

def calcular_area_circulo(radio):
    return 3.14 * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * 3.14 * radio

radio = int(input('Ingrese el radio del círculo: '))

print('area: ', calcular_area_circulo(radio))
print('perimetro: ', calcular_perimetro_circulo(radio))


'''
5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
'''

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input('Ingrese la cantidad de segundos: '))

print('horas: ', segundos_a_horas(segundos))


'''
6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.
'''

def tabla_multiplicar(numero):
    return f'''
            {numero} * 1 = {numero}
            {numero} * 2 = {numero * 2}
            {numero} * 3 = {numero * 3}
            {numero} * 4 = {numero * 4}
            {numero} * 5 = {numero * 5}
            {numero} * 6  = {numero * 6}
            {numero} * 7  = {numero * 7}
            {numero} * 8  = {numero * 8}
            {numero} * 9  = {numero *  9}
            {numero} * 10 = {numero * 10}
        '''

numero = int(input('Ingrese un número: '))

print(tabla_multiplicar(numero))


'''
7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
'''

def operaciones_basicas(a,b):
    return (a+b, a-b, a*b, a/b)

a = int(input('Ingrese el primer número : '))
b = int(input('Ingrese el segundo número : '))

resultados = operaciones_basicas(a,b)

print(f'''
            a + b = {resultados[0]}
            a - b = {resultados[1]}
            a * b = {resultados[2]}
            a / b = {resultados[3]}
    ''')


'''
8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
'''

def calcular_imc(peso,altura):
    return peso / (altura**2)

peso = int(input('Ingrese su peso: '))
altura = float(input('Ingrese su altura : '))

print(f'IMC = {calcular_imc(peso,altura):.2f} ')


'''
9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
'''

def celcius_a_fahrenheit(celcius):
    return (celcius * 9/5) + 32

celcius = float(input('Ingrese la cantidad de Celcius: '))

print('Fahrenheit:', celcius_a_fahrenheit(celcius))


'''
10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
'''

def calcular_promedio(a,b,c):
    return (a+b+c) / 3

a = int(input('Ingrese el primer número : '))
b = int(input('Ingrese el segundo número : '))
c = int(input('Ingrese el tercer número : '))

print('Promedio: ', calcular_promedio(a,b,c))
