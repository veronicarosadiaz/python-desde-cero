#lista con 10 valores aleatorios
#y luego muestre en pantalla cada elemento de la lista
#junto con su cuadrado y su cubo

#función que implementa librerías para números aleatorio
import random
lista_numeros = []
#primer recorrido de la lista, añadiendo valores aleatorios:
for indice in range(1,11):
    lista_numeros.append(random.randint(1,10))

#segundo recorrido para mostrar el resultado
for numero in lista_numeros:
    print(numero," ", numero ** 2," ", numero ** 3," ")
