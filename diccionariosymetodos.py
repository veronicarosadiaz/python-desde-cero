#para crear un diccionario se usan llaves
diccionario = {'one': 1, 'two': 2, 'three': 3}
type(diccionario)

dict1={}
#para introducir elementos en un diccionario ya existente usamos corchetes
dict1["nombre"]="ana"
dict1["edad"]=20

#ver el contenido
diccionario

#longitud del diccionario
len(dict1)

#buscar un elemento en el diccionario
"nombre" in dict1

#copiar un diccionario en otro
dict2=dict1.copy()

#borrar los elementos de un diccionario
dict1.clear

#un diccionario no tiene los elementos ordenados
#ver el valor de un elemento del diccionario
dict1.get("nombre")
#la segunda opción es lo que muestra si no existe
dict1.get("casa", "no existe")

#eliminar y mostrar un elemento como en las listas
dict1.pop("edad", "no existe")

#recorrer las claves de un diccionario
for clave in dict1.keys():
    print(clave)

#recorrer los valores:
for valor in dict1.values():
    print(valor)

#recorrer las dos cosas:
for clave, valor in dict1.items():
    print(clave,valor)