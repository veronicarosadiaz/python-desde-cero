#Pedir el nombre y los dos apellidos de una persona
#y mostrar las iniciales

nombre = input("Dime tu nombre:")
apellido1= input("Dime tu primer apellido: ")
apellido2=input("Dime tu segundo apellido:")

#La inicial sera el primer caracter de la cadena de
#caracteres almacenada en cada una de las variables.
inicial = nombre[0]
inicial = inicial + apellido1[0]
inicial = inicial + apellido2[0]

#Pasamos los caracteres a mayusculas
inicial=inicial.upper()
print("Las iniciales son: ",inicial)