#hemos introducido una cadena por teclado que representa una frase
#(palabras separadas por espacios), realiza un programa que cuente
#cuántas palabras tiene.
contador=0
posicion=0
cadena = input("Introduce una serie de palabras:")
#elimino los posibles espacios al principio y al final
cadena = cadena.strip()
#voy buscando los espacios
posicion = cad.find(" ", posicion)
while posicion != -1:
    contador = contador + 1
    while cadena[posicion + 1] == " ":
        posicion = posicion + 1
    posicion = cad.find(" ", posicion + 1)
print ("La frase tiene", contador + 1, "palabras.")
