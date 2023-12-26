# Escriba un programa que entregue la suma de los primeros n números naturales, siendo n ingresado por el usuario.
# Matemáticamente lo que se pide que haga el programa es realizar la siguiente sumatoria.
# S1=∑i=1ni=1+2+3+4+5+6+⋯+n
# Además, obtenga el resultado de la siguiente fórmula.
# S2n×(n+1)/2
# El programa debe entregar el resultado diciendo si S1 y S2 son iguales o no.

numero=int(input("Ingrese un número: "))

for i in range(1, numero+1):
    S1=i
    S1+=i

S2=(numero*(numero+1))//2

print(f"S1:{S1}")
print(f"S2:{S2}")

if S1 == S2:
    print("Son iguales")
else:
    print("No son iguales")