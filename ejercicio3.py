#Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:

def promedio(notas):
    return (f"El promeido es de {notas/4}")

for i in range(4):
    notas=float(input(f"Digite la nota {i+1}: "))
    notas+=notas

print(promedio(notas))