# gestion.py

# Inicializamos las estructuras de datos
productos_lista = []
productos_diccionario = {}

def agregar_producto(id, nombre, precio, cantidad):
    if id not in productos_diccionario:
        producto = {'id': id, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
        productos_diccionario[id] = producto
        productos_lista.append([id, nombre, precio, cantidad])
        return True
    return False

def actualizar_producto(id, nombre, precio, cantidad):
    if id in productos_diccionario:
        productos_diccionario[id] = {'id': id, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
        for producto in productos_lista:
            if producto[0] == id:
                producto[1] = nombre
                producto[2] = precio
                producto[3] = cantidad
        return True
    return False

def eliminar_producto(id):
    if id in productos_diccionario:
        del productos_diccionario[id]
        productos_lista[:] = [p for p in productos_lista if p[0] != id]
        return True
    return False

def consultar_producto(id):
    producto_diccionario = productos_diccionario.get(id)
    for producto in productos_lista:
        if producto[0] == id:
            producto_lista = producto
            return producto_lista, producto_diccionario
    return None, producto_diccionario
