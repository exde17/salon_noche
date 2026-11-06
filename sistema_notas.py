# Sistema de notas de estudiantes
# Usa listas, diccionarios, funciones, ciclos y condicionales


# Función para pedir una nota válida entre 0 y 5
def pedir_nota(nombre):
    while True:
        nota = float(input("Ingresa la nota de " + nombre + " (0 a 5): "))
        if nota >= 0 and nota <= 5:
            return nota
        else:
            print("Nota inválida, debe estar entre 0 y 5")


# Función para registrar un estudiante en la lista
def registrar_estudiante(estudiantes):
    nombre = input("Ingresa el nombre del estudiante: ")
    nota = pedir_nota(nombre)

    estudiante = {"nombre": nombre, "nota": nota}
    estudiantes.append(estudiante)
    print(nombre, "fue registrado correctamente")


# Función que dice si la nota gana o pierde
def resultado(nota):
    if nota >= 3.0:
        return "GANÓ"
    else:
        return "PERDIÓ"


# Función para mostrar todos los estudiantes con su resultado
def mostrar_estudiantes(estudiantes):
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados")
        return

    print("\n--- Lista de estudiantes ---")
    for estudiante in estudiantes:
        print(estudiante["nombre"], "sacó", estudiante["nota"], "y", resultado(estudiante["nota"]))


# Función para calcular el promedio del grupo
def calcular_promedio(estudiantes):
    suma = 0
    for estudiante in estudiantes:
        suma = suma + estudiante["nota"]
    return suma / len(estudiantes)


# Función para buscar al estudiante con la mejor nota
def mejor_estudiante(estudiantes):
    mejor = estudiantes[0]
    for estudiante in estudiantes:
        if estudiante["nota"] > mejor["nota"]:
            mejor = estudiante
    return mejor


# Función para mostrar las estadísticas del grupo
def mostrar_estadisticas(estudiantes):
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados")
        return

    ganaron = 0
    perdieron = 0
    for estudiante in estudiantes:
        if estudiante["nota"] >= 3.0:
            ganaron = ganaron + 1
        else:
            perdieron = perdieron + 1

    mejor = mejor_estudiante(estudiantes)

    print("\n--- Estadísticas ---")
    print("Total de estudiantes:", len(estudiantes))
    print("Ganaron:", ganaron)
    print("Perdieron:", perdieron)
    print("Promedio del grupo:", round(calcular_promedio(estudiantes), 2))
    print("Mejor nota:", mejor["nombre"], "con", mejor["nota"])


# Programa principal con menú
estudiantes = []  # Lista dinámica de diccionarios
opcion = ""

while opcion != "4":
    print("\n===== MENÚ =====")
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Ver estadísticas")
    print("4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        registrar_estudiante(estudiantes)
    elif opcion == "2":
        mostrar_estudiantes(estudiantes)
    elif opcion == "3":
        mostrar_estadisticas(estudiantes)
    elif opcion == "4":
        print("¡Hasta luego!")
    else:
        print("Opción no válida, intenta de nuevo")
