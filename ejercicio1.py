#Escribir una función que determine si una cadena es un palíndromo (se lee igual en ambos sentidos) o no:


def palindromo(cadena):
    cadena = cadena.lower() #Cambiamos todas las mayúculas a minúsculas
    cadena = cadena.replace(" ","") #Quitamos todos los espacios
    cadena = cadena.replace("á", "a") #Remmplazamos las palabras con tilde con una palabra normal.
    cadena = cadena.replace("é", "e")
    cadena = cadena.replace("í", "i")
    cadena = cadena.replace("ó", "o")
    cadena = cadena.replace("ú", "u")
    
    a = 0 #Indicamos que la primera letra tiene el índice 0
    b = len(cadena) - 1 #La última letra tiene el índice -1

    for i in range(0, len(cadena)): 
        if cadena[a] == cadena[b]: #comprobamos si la letra en el índice 0 es igual a la letra del índice final
            a += 1 #Incrementamos la variable a en 1
            b -=1 #Restamos a la variable b en 1
        else:
            return False #Si no se cumple que la palabra es palidormo nos retornará False
    return True

cadena = input("Ingrese una palabra o frase: ")

if palindromo(cadena):
    print("Es una palabra o frase Palindromo")
else:
    print("No una palabra o frase Palindromo")




