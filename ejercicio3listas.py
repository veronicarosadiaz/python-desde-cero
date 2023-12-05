#programa que lee por teclado las 5 notas obtenidas
#por un alumno (0-10) y luego muestre todas las notas de los alumnos,
#su nota media, la nota más alta y la más baja.

notas = []
for indice in range(1,6):
    while True:
        nota = int(input("Introduce la nota %d:" % indice))
        if nota >=0 and nota <=10: break
    notas.append(nota)

print("Notas ", end="")
for nota in notas:
    print(nota," ",end="")
print()
print("Nota media: ",sum(notas)/len(notas))
print("Nota máxima: ",max(notas))
print("Nota mínima: ",min(notas))