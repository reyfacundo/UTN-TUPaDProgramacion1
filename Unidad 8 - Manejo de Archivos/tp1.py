# 1) Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt 
# con tres productos. Cada línea debe tener: nombre,precio,cantidad
lineas_iniciales = [
    "Lapicera,120.5,30\n",
    "Cuaderno,250,15\n",
    "Mochila,1200,5\n"
]

with open("productos.txt", "w") as archivo:
    archivo.writelines(lineas_iniciales)


# 2) Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea,
# la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

# 4) Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos 
# en una lista llamada productos, donde cada elemento sea un diccionario con claves: nombre, precio, cantidad
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        productos.append({
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        })

for prod in productos:
    print(f"Producto: {prod['nombre']} | Precio: ${prod['precio']} | Cantidad: {prod['cantidad']}")


# 3) Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos, 
# le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad) y lo agregue al archivo 
# sin borrar el contenido existente
nuevo_producto = input("Ingresá nuevo producto (nombre,precio,cantidad): ")
nombre, precio, cantidad = nuevo_producto.strip().split(",")
productos.append({
    "nombre": nombre,
    "precio": float(precio),
    "cantidad": int(cantidad)
})


# 5) Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. 
# Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. 
# Si no existe, mostrar un mensaje de error
buscar = input("Ingresá el nombre del producto a buscar: ")
encontrado = False
for prod in productos:
    if prod["nombre"].lower() == buscar.lower():
        print(f"Producto: {prod['nombre']} | Precio: ${prod['precio']} | Cantidad: {prod['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("Producto no encontrado.")


# 6) Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, 
# sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados desde la lista
with open("productos.txt", "w") as archivo:
    for prod in productos:
        archivo.write(f"{prod['nombre']},{prod['precio']},{prod['cantidad']}\n")
