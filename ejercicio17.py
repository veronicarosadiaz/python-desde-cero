#hora de llegada de un ciclista
#se pide la hora de salida en horas, minutos y segundos
#se pide el numero de segundos que tardó en llegar
#se calcula la hora a la que llegó

horapartida = int(input("Hora de salida:"))
minpartida = int(input("Minutos de salida:"))
segpartida = int(input("Segundos de salida:"))
segviaje = int(input("Segundos que has tardado en hacer el viaje:"))

#Necesitamos convertir la hora de salida en segundos:
seginicial = horapartida * 3600 + minpartida * 60 + segpartida;

#Sumamos los segundos que ha tardado
segfinal = seginicial + segviaje;

#Pasamos el total de segundos a formato horas, minutos y segundos
horallegada = segfinal // 3600;
#utilizo la división entera porque necesito un número entero de horas, sin decimales

minllegada = (segfinal % 3600) // 60;
#el resto de la división me da el número de segundos sobrantes, que no son
#suficientes para llegar a una hora, y lo divido entre 60 para sacar un número
#entero de minutos.

segllegada = (segfinal % 3600) % 60;
#el resto de la división entre los segundos sobrantes del total de horas y el resto de
#la división para hallar los minutos me da los segundos sobrantes que no son suficientes
#para llegar a otro minuto.

print("Hora de llegada:")
print(horallegada,":",minllegada,":",segllegada,":")