# Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.
# El promedio del ramo se calcula con la siguiente formula.

#     NC=(C1+C2+C3)/3
#     NF=NC*0.7 + NL*0.3

# Donde NC es el promedio de certámenes, NL el promedio de laboratorio y NF la nota final.
# Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.

def notaFinal(certamen1, certamen2, notaLaboratorio):
    NC= (certamen1 + certamen2 + 60) / 3
    NF= NC * 0.7 + notaLaboratorio * 0.3
    return (f"Necesita nota {NF} en el certamen 3")

certamen1=int(input("Ingrese la nota del certamen 1: "))
certamen2=int(input("Ingrese la nota del certamen 2: "))
notaLaboratorio=int(input("Ingrese la nota del laboratorio: "))

print(notaFinal(certamen1,certamen2,notaLaboratorio))