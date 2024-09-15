# validaciones.py
import re

def validar_producto(id, nombre, precio, cantidad):
    if not (isinstance(id, str) and id and isinstance(nombre, str) and nombre):
        return False
    if not (isinstance(precio, (int, float)) and precio > 0):
        return False
    if not (isinstance(cantidad, int) and cantidad >= 0):
        return False
    return True

def validar_email(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) is not None

def validar_telefono(telefono):
    return re.match(r'^\+54\s9\s\d{2}\s\d{4}-\d{4}$|^011\s\d{4}-\d{4}$', telefono) is not None

def validar_codigo_postal(codigo_postal):
    return re.match(r'^\d{4}$|^[A-Z]\d{4}[A-Z]{3}$', codigo_postal) is not None

def validar_fecha(fecha):
    return re.match(r'^\d{4}-\d{2}-\d{2}$', fecha) is not None
