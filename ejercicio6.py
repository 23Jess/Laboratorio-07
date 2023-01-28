#Escribir una función que reemplace todas las apariciones de una subcadena en una cadena dada con otra subcadena dada.


palabra = "Python es un lenguaje de programación más usado"
palabra_reemplazada = " "
for subcadena in palabra:
    if subcadena=="e":
        subcadena="Java"
    palabra_reemplazada += subcadena
print(palabra_reemplazada)

#Otro método
cadena = "LA PROGRAMACIÓN ES LA NUEVA ERA."
for c in range(1):
    letra = input("Digite una letra: ").upper()
    nueva = cadena.replace("A", letra) #reemplaza el caracter a de la variable cadena con el contenido de la variable letra
    print(" Nueva cadena: ", nueva)

