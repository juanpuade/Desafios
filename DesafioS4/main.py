# main.py
from gestion import (
    agregar_producto, actualizar_producto, eliminar_producto, consultar_producto,
    productos_lista, productos_diccionario
)
from validaciones import validar_email, validar_telefono, validar_codigo_postal, validar_fecha

def imprimir_menu():
    """ Imprime el menú de opciones """
    print("Sistema de Gestión de Productos")
    print("1. Agregar Producto")
    print("2. Actualizar Producto")
    print("3. Eliminar Producto")
    print("4. Consultar Producto")
    print("5. Validar Datos")
    print("0. Salir")

def obtener_opcion():
    """ Obtiene la opción del usuario """
    try:
        opcion = int(input("Seleccione una opción: "))
        return opcion
    except ValueError:
        print("Opción no válida. Intente nuevamente.")
        return -1

def obtener_datos_producto():
    """ Obtiene los datos del producto del usuario para agregar """
    id = input("Ingrese el ID del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    try:
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
    except ValueError:
        print("Precio o cantidad no válidos.")
        return id, None, None, None
    return id, nombre, precio, cantidad

def obtener_id_producto():
    """ Obtiene el ID del producto del usuario para operaciones CRUD """
    return input("Ingrese el ID del producto: ")

def producto_existe(id):
    """ Verifica si el producto existe en la lista o el diccionario """
    return id in productos_diccionario or any(p[0] == id for p in productos_lista)

def main():
    while True:
        imprimir_menu()
        opcion = obtener_opcion()

        if opcion == 0:
            print("Saliendo...")
            break
        elif opcion == 1:  # Agregar Producto
            id, nombre, precio, cantidad = obtener_datos_producto()
            if not nombre or precio is None or cantidad is None:
                print("Datos del producto no válidos.")
                continue
            if agregar_producto(id, nombre, precio, cantidad):
                print("Producto agregado.")
            else:
                print("Producto ya existe.")
        elif opcion == 2:  # Actualizar Producto
            id = obtener_id_producto()
            if producto_existe(id):
                nombre = input("Ingrese el nuevo nombre del producto: ")
                try:
                    precio = float(input("Ingrese el nuevo precio del producto: "))
                    cantidad = int(input("Ingrese la nueva cantidad del producto: "))
                except ValueError:
                    print("Precio o cantidad no válidos.")
                    continue
                if actualizar_producto(id, nombre, precio, cantidad):
                    print("Producto actualizado.")
                else:
                    print("Producto no encontrado.")
            else:
                print("Producto no encontrado.")
        elif opcion == 3:  # Eliminar Producto
            id = obtener_id_producto()
            if eliminar_producto(id):
                print("Producto eliminado.")
            else:
                print("Producto no encontrado.")
        elif opcion == 4:  # Consultar Producto
            id = obtener_id_producto()
            producto_lista, producto_diccionario = consultar_producto(id)
            if producto_lista:
                print(f"Producto en lista: {producto_lista}")
            else:
                print("Producto no encontrado en la lista.")
            if producto_diccionario:
                print(f"Producto en diccionario: {producto_diccionario}")
            else:
                print("Producto no encontrado en el diccionario.")
        elif opcion == 5:
            email = input("Ingrese el email para validar: ")
            telefono = input("Ingrese el teléfono para validar: ")
            codigo_postal = input("Ingrese el código postal para validar: ")
            fecha = input("Ingrese la fecha para validar (YYYY-MM-DD): ")

            print(f"Email válido: {validar_email(email)}")
            print(f"Teléfono válido: {validar_telefono(telefono)}")
            print(f"Código postal válido: {validar_codigo_postal(codigo_postal)}")
            print(f"Fecha válida: {validar_fecha(fecha)}")
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
