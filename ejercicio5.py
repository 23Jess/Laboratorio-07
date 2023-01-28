#Escribir una función que determine la longitud de la subcadena más larga que contiene solo dígitos.

def lontitud_digitos(cadena):
    digitos = 0 #variable para conteo de dígitos

    for i in cadena:
        if i.isdigit(): #usamos la condicion para saber si es dígito
            digitos += 1 #si se cumple incrementamos en una unidad la variable
        else:
            pass  #si no se cumple se hace caso omiso
    return digitos

texto = input("Digite un texto: ")
resultado = lontitud_digitos(texto)

print("La longitud de digitos es: ",resultado )