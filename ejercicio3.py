# Escriba un programa que permita determinar el número mayor perteneciente a un conjunto de n números, donde tanto el valor de n como el de los números deben ser ingresados por el usuario.

cantidad=int(input("Cuantos números desea ingresar?: "))

for i in range(1, cantidad+1):
    numero=int(input("Ingrese un número: "))
    mayor=numero
    if mayor<numero:
        mayor=numero

print(f"El mayor es {mayor}")