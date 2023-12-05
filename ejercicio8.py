 # Guardar los nombres y las edades de los alumnos de un curso.
 # Realiza un programa que introduzca el nombre y la edad de cada alumno.
 # El proceso de lectura de datos terminará cuando se introduzca com nombre
 # un asterisco. Al finalizar se mostrarán los siguientes datos:
 # * Todos los alumnos mayores de edad.
 # * Los alumnos que tienen más edad.

 # no es mejor hacerlo con un diccionario??? por qué con listas???

nombres = []
edades = []

while True:
    nombre = input("Dime el nombre de un alumno:")
    if nombre != "*":
        nombres.append(nombre)
        edades.append(int(input("Dime su edad:")))
    if nombre == "*": break;

#edad máxima
edad_max = max(edades)

#mayores de edad
print("Alumnos mayores de edad:")
for nombre, edad in zip(nombres, edades):
    if edad >= 18:
        print(nombre)

#alumnos más mayores
print("Alumnos que tienen más edad:")
for nombre, edad in zip(nombres, edades):
    if edad == edad_max:
        print(nombre)
