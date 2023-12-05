#algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.abs

tabla = int(input("Dime un número: "))
for num in range(1,11):
    print("%d * %d = %d" % (num,tabla,num*tabla))