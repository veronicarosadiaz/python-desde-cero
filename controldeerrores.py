while True:
    try:
        x= int(input("Introduce un número:"))
        break
    except ValueError:
        print("Debes introducir un número")

#(similar al try catch en powershell)

cad=input("Dime un número:")
try:
    print (10/int(cad))
except ValueError:
    print("No se puede convertir a entero")
except ZeroDivisionError:
    print("No se puede dividir por cero")
else:
    print("Se ha producido otro error")
#se ejecuta siempre al final de la estructura:
finally:
    print("Se ejecuta siempre al final")