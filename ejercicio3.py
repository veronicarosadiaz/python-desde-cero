#Dados los catetos de un triángulo rectángulo,
#calcular su hipotenusa.
import math
cateto1 = float(input("Introduce el cateto 1:"))
cateto2 = float(input("Introduce el cateto 2:"))
hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)
#una opción
print ("La hipotenusa es", hipotenusa)
#otra opción para imprimir un número real (float) con dos decimales
print("La hipotenusa es %.2f" % hipotenusa)

