#lista de listas
# crear una tabla (lista de dos dimensiones) de 5x5 enteros
# cargar la tabla con valores numéricos enteros
# sumar todos los elementos de cada fila y todos los elementos de cada columna

tabla = []
for indice_fila in range(1,6):
    fila = []
    for indice_columna in range(1,6):
        fila.append(int(input("Introduce el número de la fila %d y columna %d: " % (indice_fila,indice_columna))))
    tabla.append(fila)

#sumar las filas
indice_fila=1
for fila in tabla:
    print("La suma de los elementos de la fila %d es %d" % (indice_fila,sum(fila)))
    indice_fila +=1

#sumar las columnas
for indice_columna in range(1,6):
    suma=0
    for fila in tabla:
        suma=suma + fila[indice_columna - 1]
        print("La suma de los elementos de la columna %d es %d" %  (indice_columna,suma)

#"a esto hay que esharle un rato"