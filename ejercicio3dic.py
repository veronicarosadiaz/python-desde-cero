#diccionario que almacena los nombres y precios
#de distintas frutas. El programa pedirá el nombre de la fruta
#y la cantidad que se ha vendido y nos mostrará el precio final
#de la fruta a partir de los datos guardados en el diccionario. 
#si la fruta no existe nos dará un error.
#tras cada consulta el programa nos pregunta si queremos hacer otra consulta

precios = {"platano": 4, "manzana": 2, "naranja": 1.5, "piña": 3}
while True:
    fruta = input("Dime la fruta que has vendido:")
    if fruta.lower() not in precios:
        print("La fruta no existe.")
    else: 
        cantidad=int(input("Dime la cantidad de frutas que has vendido:"))
        print("El precio es de %f" % (cantidad * precios[fruta,lower()]))
    opcion = input("¿Quieres vender otra fruta? (S/N)")
    while opcion.lower() != "s" and opcion.lower() != "n":
        opcion = input("¿Quieres vender otra fruta? (S/N)")
    if opcion.lower() == "n":
        break