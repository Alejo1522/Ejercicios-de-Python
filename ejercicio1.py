# Escriba un programa que pida al usuario que escriba su nombre, y lo salude llamándolo por su nombre.

def mensaje(nombre):
    return (f"Hola, {nombre}")

nombre=input("Ingrese su nombre: ")

print(mensaje(nombre))