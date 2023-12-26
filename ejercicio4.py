#Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por cuántas letras lo es.

def convercion(palabra_1, palabra_2):
    longitud1=len(palabra_1)
    longitud2=len(palabra_2)

    if longitud1 > longitud2:
        cantidad_letras=longitud1 - longitud2
        return (f"La palabra {palabra_1} tiene {cantidad_letras} letras mas que {palabra_2}.")
    elif longitud1 < longitud2:
        cantidad_letras=longitud2 - longitud1
        return (f"La palabra {palabra_2} tiene  {cantidad_letras} letras mas que {palabra_1}.")
    else:
        return ("Las dos palabras tienen el mismo largo")
    
palabra_1=input("Ingrese una palabra: ")
palabra_2=input("Ingrese otra palabra: ")

print(convercion(palabra_1, palabra_2))