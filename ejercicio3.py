#Escribir una función que divida una cadena dada en una
#lista de subcadenas cada vez que aparezca un carácter
#específico.


def dividir_caracter(cadena, caracter):
    cadena_separada = cadena.split(caracter) #el método split() retornará una lista con el contenido de la variable cadena_separada
    return cadena_separada

print(dividir_caracter("Python es un lenguaje de programacion", "n"))
