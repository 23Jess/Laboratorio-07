#Escribir una función que determine la longitud de la subcadena más larga que no contiene ninguna letra repetida.

def longitud_subcadena(frase):
    palabras = frase.split() #particionamiento de la frase a partir del caracter de espacio

    masLarga = palabras[0]

    for i in range(1, len(palabras)): #Calculamos la longitud de las palabras
        if len(masLarga) < len(palabras[i]):
            masLarga = palabras[i]

    print(len(masLarga))
    return masLarga

frase = input("Ingrese la frase: ")
print(longitud_subcadena(frase))
