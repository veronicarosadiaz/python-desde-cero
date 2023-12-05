#función que lea y almacene día, mes y año
def LeerFecha():
    day = int(input("Día: "))
    month = int(input("Mes: "))
    year = int(input("Año: "))
    return day,month,year

#función que mire si un año es bisiesto:
def EsBisiesto(year):
    return (year % 4 == 0 and not (year % 100 == 0)) or year % 400 == 0


#funcion que calcule los días del mes
def DiasDelMes(month,year):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif  month in [4,6,9,11]:
        return 30
    elif month == 2:
        if EsBisiesto(year):
            return 29
        else:
            return 28




#función que calcule el día juliano

def CalcularDiaJuliano(day,month,year):
    diajuliano=0
    for mes in range(1,month):
        diajuliano = diajuliano + DiasDelMes(mes,year)
    diajuliano=diajuliano + day
    return diajuliano


#queremos crear un programa que al introducir una fecha
#nos diga el día juliano que corresponda (número de día en el año)

d,m,a = LeerFecha()
print("Día Juliaon: ", CalcularDiaJuliano(d,m,a))