#Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:
nota=0
def promedio(nota):
    return (f"El promeido es de {nota/4}")

for i in range(4):
    notas=float(input(f"Digite la nota {i+1}: "))
    nota=nota+notas

print(promedio(nota))