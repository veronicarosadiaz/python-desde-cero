# Crea una aplicación que pida un número y calcule su factorial
# producto de todos los enteros entre 1 y el propio número
# se representa con el número seguido de un signo de exclamación
# TODO LO QUE PODEMOS HACER CON UN WHILE SE PUEDE HACER CON UN FOR
# Y VICEVERSA

#versión 1
resultado = 1;
num=int(input("Dime un número:"))
contador = 2;

while contador <= num:
    resultado = resultado * contador;
    contador = contador + 1;
print("El resultado es", resultado)

#versión 2
resultado = 1;
num=int(input("Dime un número:"))

for contador in range(2, num+1):
    resultado = resultado * contador;
print("El resultado es", resultado)
