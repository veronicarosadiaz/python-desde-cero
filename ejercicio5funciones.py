#función que recibe una lista de números enteros y devuelve el máximo y el mínimo
#de los números guardados en el vector.
#parámetros de entrada: lista de enteros
#valores de salida: valor máximo y mínimo
import random
def CalcularMaxMin(lista):
    return(max(lista),min(lista))

#programa que pida números por teclado y muestre el máximo y el mínimo

numeros = []

#inicializo la lista con valores aleatorios:
for i in range(10):
    numeros.append(random.randint(1,100))
vmax,vmin = CalcularMaxMin(numeros)
print("El valor máximo es ", vmax)
print("El valor mínimo es ", vmin)