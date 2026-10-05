nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

calificacion1 = float(input("Ingresa primera calificación: "))
calificacion2 = float(input("Ingresa segunda calificación: "))
calificacion3 = float(input("Ingresa tercera calificación: "))

promedio = (calificacion1 + calificacion2 + calificacion3) / 3

print("\nNombre:", nombre)
print("Edad:", edad)
print("Promedio:", promedio)

if promedio >= 71:
    print("Aprobado")
else:
    print("No aprobado")
