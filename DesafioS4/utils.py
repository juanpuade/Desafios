# utils.py
from validaciones import validar_email, validar_telefono, validar_codigo_postal, validar_fecha

def imprimir_menu():
    print("Sistema de Gestión de Productos")
    print("1. Agregar Producto")
    print("2. Actualizar Producto")
    print("3. Eliminar Producto")
    print("4. Consultar Producto")
    print("5. Validar Datos")
    print("0. Salir")

def obtener_opcion():
    try:
        return int(input("Seleccione una opción: "))
    except ValueError:
        return -1

def obtener_datos_producto():
    id = input("Ingrese el ID del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    return id, nombre, precio, cantidad
