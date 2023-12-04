#!/usr/bin/python3
#librería para parámetros:
import sys
params=sys.argv[1:]
#mostrar los parámetros a partir del primero (el 0 es el nombre del script)

if len(params) !=2:
    print("error")
else:
    a=int(params[0])
    b=int(params[1])
    resultado=num1 + num2
    print("Resultado: ", resultado)

