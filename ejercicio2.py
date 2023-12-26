# Escriba un programa que indique si un año es bisiesto o no, teniendo en cuenta cuál era el calendario vigente en ese año:

def es_bisiesto(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return (f"{year} es bisiesto")
    else:
        return (f"{year} no es bisiesto")

year=int(input("Ingrese un año: "))

print(es_bisiesto(year))