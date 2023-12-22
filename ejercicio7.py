#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas

def Hora(horaActual, horaFutura):
    return (f"En {horaFutura} horas, el reloj marcara las {(horaActual+horaFutura)%24}")

horaActual=int(input("Ingrese la hora actual (en formato de 24 horas): "))
horaFutura=int(input("Ingrese el número enter de horas a avanzar: "))

print(Hora(horaActual,horaFutura))