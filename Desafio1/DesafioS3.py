# Matriz de productos 
productos = []

# Funciones CRUD

# 1. Crear 
def crear_producto(nombre, descripcion, precio, cantidad):
    nombre = nombre[:20].upper()  # Convertir a mayúsculas
    descripcion = descripcion[:30]
    
    # Crear un nuevo producto como una lista
    producto = [nombre, descripcion, float(precio), int(cantidad)]
    
    # Agregar el producto a la lista de productos
    productos.append(producto)

# 2. Leer mostrar todos los productos
def leer_productos():
    print(f"{'Nombre':<20} {'Descripción':<30} {'Precio':<10} {'Cantidad':<10}")
    print("-" * 70)
    for producto in productos:
        print(f"{producto[0]:<20} {producto[1]:<30} {producto[2]:<10.2f} {producto[3]:<10}")

# 3. Editar un producto existente por índice
def actualizar_producto(indice, nombre=None, descripcion=None, precio=None, cantidad=None):
    if 0 <= indice < len(productos):
        if nombre:
            productos[indice][0] = nombre[:20].upper()  # Limitar y convertir a mayúsculas
        if descripcion:
            productos[indice][1] = descripcion[:30]  # Limitar longitud
        if precio:
            productos[indice][2] = float(precio)
        if cantidad:
            productos[indice][3] = int(cantidad)
    else:
        print("Índice fuera de rango.")

# 4. Eliminar un producto por índice
def eliminar_producto(indice):
    if 0 <= indice < len(productos):
        productos.pop(indice)
    else:
        print("Índice fuera de rango.")

# Ordenar la matriz
# Ordenar primero por precio y por nombre 
def ordenar_productos():
    productos.sort(key=lambda x: (x[2], x[0]))

def actualizar_producto(indice, nombre=None, descripcion=None, precio=None, cantidad=None):
    if nombre is not None:
        productos[indice][0] = nombre
    if descripcion is not None:
        productos[indice][1] = descripcion
    if precio is not None:
        productos[indice][2] = precio
    if cantidad is not None:
        productos[indice][3] = cantidad


# Menú para interactuar con el sistema
def menu():
    while True:
        print("\n--- Menú CRUD ---")
        print("1. Crear producto")
        print("2. Leer productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Ordenar productos")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ")
            precio = input("Precio: ")
            cantidad = input("Cantidad: ")
            crear_producto(nombre, descripcion, precio, cantidad)
        elif opcion == '2':
            leer_productos()
        elif opcion == '3':
            indice = int(input("Índice del producto a actualizar: "))
            nombre = input("Nuevo nombre (dejar vacío si no deseas cambiar): ")
            descripcion = input("Nueva descripción (dejar vacío si no deseas cambiar): ")
            precio = input("Nuevo precio (dejar vacío si no deseas cambiar): ")
            cantidad = input("Nueva cantidad (dejar vacío si no deseas cambiar): ")
           actualizar_producto(indice, nombre, descripcion, precio, cantidad)

        elif opcion == '4':
            indice = int(input("Índice del producto a eliminar: "))
            eliminar_producto(indice)
        elif opcion == '5':
            ordenar_productos()
            print("Productos ordenados.")
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

menu()
