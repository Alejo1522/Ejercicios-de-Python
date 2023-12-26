# Escriba un programa para que reconozca oraciones palíndromas. La dificultad radica en que hay que ignorar los espacios:

def crear_palindromo(frase):
    fraseSinEspacios=''.join(frase.split()).lower()
    return fraseSinEspacios == fraseSinEspacios[::-1]

frase=input("Ingrese palabra: ")

resultado=crear_palindromo(frase)

if resultado:
    print("Es palindromo")
else:
    print ("No es palindromo")