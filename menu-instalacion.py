#!/bin/usr/env python
#importamos comandos de sistema operativo:
import os

print("----MENÚ INSTALACIÓN----")
print("1. Reiniciar el sistema")
print("2. Apagar el sistema")
print("3. Cerrar sesión")
print("4. Salir")
opcion=input("Elija una opción:")

if opcion == 1:
    os.system("reboot")
elif opcion == 2:
    os.system("shutdown +2")
elif opcion == 3:
    usuario = os.getenv('USER')
    os.system(f"pkill -u {usuario}")
elif opcion == 4:
     exit
else:
    print("Opción incorrecta. Vuelva a intentarlo")
