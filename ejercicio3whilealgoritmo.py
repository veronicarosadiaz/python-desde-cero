#Algoritmo que pide números hasta que se introduzca un cero.abs#
# Debe mostrar la suma de todos los números
# y la media de todos los números

#VERSIÓN 1
#crear un acumulador de valores:
suma=0
#crear un contador para poder hallar cuántos números he introducido
#y así hallar la media entre todos ellos:
contador=0
num=int(input ("Número (Introduce 0 para salir):"))
while num!= 0:
    suma = suma + num
    contador = contador + 1
    num=int(input ("Número (Introduce 0 para salir):"))

#si el contador está a cero no se puede hacer la división
if contador > 0:
    media = suma / contador
else:
    media = 0

print("La suma de todos los números introducidos es", suma)
print("La media de todos los números introducidos es", media)

#VERSIÓN 2
suma=0
contador=0
while True:
    num=int(input("Número (Introduce 0 para salir):"))
    suma=suma+num
    #si el número es cero no tenerlo en cuenta
    if num !=0:
        contador = contador + 1
    if num ==0:
        break

#si el contador está a cero no puedo hacer la división
if contador > 0:
    media = suma / contador
else:
    media = 0

print("La suma de todos los números introducidos es", suma)
print("La media de todos los números introducidos es", media)