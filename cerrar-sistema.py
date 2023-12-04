#!/usr/bin/env python3
import os

opcion=""
while opcion < "a" or opcion > "c":
    print ("a. Cerrar sesión")
    print ("b. Apagar el sistema")
    print ("c. Reiniciar el sistema")
    opcion = input("Elija una opción:").lower()

if opcion == "a":
    print("Cerrando sesión")
elif opcion =="b":
    print("Apagando el sistema")
elif opcion == "c":
    print("Reiniciando el sistema")
else:
    print("Opción incorrecta")