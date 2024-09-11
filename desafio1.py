import random

# Definir la lista de estudiantes y materias
estudiantes = ['Ana', 'Luis', 'Pedro', 'María']
materias = ['Matemáticas', 'Historia', 'Literatura', 'Ciencias']

# Crear la matriz de calificaciones
calificaciones = []
for i in range(len(estudiantes)):
    fila = [random.randint(1, 10) for j in range(len(materias))]
    calificaciones.append(fila)

# Mostrar la matriz
def mat(calificaciones):
    print("Calificaciones:")
    for i in range(len(estudiantes)):
            print(estudiantes[i], ":" , calificaciones[i])

# Calcular y mostrar el promedio de cada estudiante
def promest(calificaciones):
    print("\nPromedio por estudiante:")
    for i in range(len(estudiantes)):
        promedio = sum(calificaciones[i]) / len(materias)
        print(estudiantes[i], ":", promedio)

# Calcular y mostrar el promedio de cada materia
def prommat(calificaciones):
    print("\nPromedio por materia:")
    for j in range(len(materias)):
        suma = sum(calificaciones[i][j] for i in range(len(estudiantes)))
        promedio = suma / len(estudiantes)
        print(materias[j], ":", promedio)

# Ejecutar funciones
mat(calificaciones)
promest(calificaciones)
prommat(calificaciones)
