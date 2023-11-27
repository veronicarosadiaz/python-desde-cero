#Cálculo de calificación final, tomando:
#55% del promedio de sus tres calificaciones parciales.
#30% de la calificación del examen final.
#15% de la calificación del examen final.

import math
parcial1=float(input("Nota del primer parcial:"))
parcial2=float(input("Nota del segundo parcial:"))
parcial3=float(input("Nota del tercer parcial:"))
examen=float(input("Nota del examen:"))
trabajo=float(input("Nota del trabajo:"))

notafinal = ((parcial1 + parcial2 + parcial3)/3) * 0.55 + examen * 0.3 + trabajo * 0.15
print("La nota final es", nota)