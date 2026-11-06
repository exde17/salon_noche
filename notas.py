# Programa para pedir el nombre y la nota de 4 usuarios
# y mostrar si ganaron o perdieron

usuarios = []  # Lista vacía que se va llenando con diccionarios

for i in range(4):
    nombre = input("Ingresa el nombre del usuario " + str(i + 1) + ": ")
    nota = float(input("Ingresa la nota de " + nombre + ": "))

    usuario = {"nombre": nombre, "nota": nota}
    usuarios.append(usuario)

print("\n--- Resultados ---")

for usuario in usuarios:
    if usuario["nota"] >= 3.0:
        print(usuario["nombre"], "sacó", usuario["nota"], "y GANÓ")
    else:
        print(usuario["nombre"], "sacó", usuario["nota"], "y PERDIÓ")

# quiero ver los cambios        
