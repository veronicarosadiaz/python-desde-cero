#!/usr/bin/env python
import sys, os
import datetime
params = sys.argv[1:]

def error(msg):
     print("\033[31m" + msg, "\033[m")

if len(params) != 1:
    error("Número de parámetros incorrecto")
    exit()

#Comprobar si existe el fichero
file = params[0]
#sacar la fecha de última modificación del fichero para luego comparar si ha habido modificaciones
old_stat = None
if os.path.isfile(file):
     pid = os.getpid()
     backupfile = f"/tmp/{pid}.safedit.py"
     os.system(f"cp {file} {backupfile}")
     old_stat = os.stat(file)
     print("Creando copia de seguridad en ", backupfile)

#Abrimos el archivo indicado por parámetro con nano
os.system("nano" + file) 

#eliminar la copia de seguridad si el archivo no se ha modificado desde la última vez
if old_stat is not None and os.stat(file) == old_stat:
     os.system(f"rm {file} {backupfile}")
#también se puede hacer con: os.path.getmtime(file) para sacar la fecha de última modificación
     
     
