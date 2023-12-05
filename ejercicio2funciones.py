#función múltiplo o no
def esmultiplo(num1,num2):
    if num1 % num2== 0:
        return True
    else:
        return False

#pedir dos números para ver si uno es múltiplo de otro
#la función va a devolver dos valores (si uno es múltiple de otro, y si otro es múltiplo de uno)

numero1=int(input("Número 1:"))
numero2=int(input("Número 2:"))
if esmultiplo(numero1,numero2):
    print(numero1,"es múltiplo de",numero2)
else:
    print(numero1,"no es múltiplo de",numero2)
