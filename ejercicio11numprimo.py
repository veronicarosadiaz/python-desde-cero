# escribe un programa que diga si un número introducido por teclado
# es un número primo (divisible sólo entre 1 y sí mismo)

es_primo=True
numeroprimo = int(input("Introduce un número para comprobar si es primo: "))
for num in range(2, numeroprimo):
    if numeroprimo % num == 0:
        es_primo = False
        break

if es_primo:
    print("Es Primo")
else:
    print("No es Primo")