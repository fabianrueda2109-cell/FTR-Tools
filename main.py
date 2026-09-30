import subprocess
import random
import string
print("Bienvenido a FTR Tools")
nombre = input("Usuario: ")
print("Hola", nombre)
print("1. Calculadora\n2. Generar contraseñas\n3. Comprobador de internet\n4. Informacion del pc\n5. Conversor\n6. Herramientas de texto\n0. Salir")
opcion = input("Elige una herramienta: ")
if opcion == "1":
    numero = int(input("Numero 1: "))
    numero_2 = int(input("Numero 2: "))
    operacion = input("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\nElige una operacion: ")
    if operacion == "1":
        resultado = numero + numero_2
        print(resultado)
    elif operacion == "2":
        resultado = numero - numero_2
        print(resultado)
    elif operacion == "3":
        resultado = numero * numero_2
        print(resultado)
    elif operacion == "4":
        if numero_2 == 0:
            print("No se puede dividir entre 0")
        else:
            resultado = numero / numero_2
            print(resultado)
    else:
        print("Opción no válida")
elif opcion == "2":
    longitud = int(input("¿Cuántos caracteres quieres? "))
    if longitud <= 0:
        print("La longitud debe ser mayor que 0")
    else:
        contraseña = ""
        for i in range(longitud):
            caracteres = string.ascii_letters + string.digits + string.punctuation
            caracter = random.choice(caracteres)
            contraseña += caracter
        print(contraseña)
elif opcion == "3":
    resultado = subprocess.run(["ping", "-c", "1", "google.com"])
    if resultado.returncode == 0:
        print("Internet disponible")
    else:
        print("No hay conexión a Internet")
elif opcion == "4":
    print("Información del PC")
elif opcion == "5":
    print("Conversor")
elif opcion == "6":
    print("Herramientas de texto")
elif opcion == "0":
    print("Hasta luego")
else:
    print("Opción no válida")