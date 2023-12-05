#comprobar si una cadena contiene una subcadena
cad = input("Introduce una cadena:")
subcad = input("Introduce una subcadena:")

if cad.find(subcad) > -1:
    print("La cadena contiene la subcadena.")
else:
    print("La cadena no contiene la subcadena.")

#segunda forma, más fácil
if subcad in cad:
    print("La cadena contiene la subcadena.")
else:
    print("La cadena no contiene la subcadena.")