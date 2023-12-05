#algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.abs

for tabla in range(1, 6):
    for num in range(1, 11):
        print("%d * %d = %D" % (num, tabla, num * tabla))
