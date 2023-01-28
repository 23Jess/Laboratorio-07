#Escribir una función que determine la frecuencia de cada carácter en una cadena dada y devuelva un diccionario.

def contar_palabras(cadena):
    #Función que cuenta el número de veces que aparece cada palabra en un texto.
    #Parámetros:
    #cadena: Es una cadena de caracteres.
    #Devuelve: 
    #Un diccionario con pares palabra:frecuencia con las palabras contenidas en el texto y su frecuencia.

    cadena = cadena.split()
    palabras = {}
    for i in cadena:
        if i in palabras:
            palabras[i] += 1
        else:
            palabras[i] = 1
    return palabras

def mmas_repetido(palabras):
    max_palabra = ''
    max_frecuencia = 0
    for palabra, frecuencia in palabras.items():
        if frecuencia > max_frecuencia:
            max_palabra = palabra
            max_frecuencia = frecuencia
    return max_palabra, max_frecuencia

cadena = input("Introduzca la frase: ")
print(contar_palabras(cadena))
print(mmas_repetido(contar_palabras(cadena)))