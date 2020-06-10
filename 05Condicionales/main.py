"""

# Condicional IF

SI se_cumple_esta_condicion:
    Ejecutar grupo de instrucciones
SI NO:
Se ejecutan otro grupo de instrucciones

# Operadores de comparacion

== igual
!= diferente
< menor que
> mayor que
<= menor igual que
>= mayor igual que


# Operadores logicos
and Y
or O
! negacion
not NO

"""






# Ejemplo 1

print("#################### EJEMPLO 1 ####################")


#color = input("Adivina cual es mi color favorito:")
color = "rojo"
if color == "rojo":
    print("Mi color favorito es ROJO")
else:
    print("El color que ingresaste no es mi favorito!")


# Ejemplo 2

print("\n#################### EJEMPLO 2 ####################")

year = 2020
#year = int(input("En qué año estamos?"))

if year >= 2021:
    print("Estamos a 2021 en adelante!!")
else:
    print("Es un año anterior a 2021")


# Ejemplo 3

print("\n#################### EJEMPLO 3 ####################")

nombre = "Eduardo Onofre"
ciudad = "Saltillo"
continente = "Asia"
edad = 18
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad!")

    if continente != "America":
        print("No es Americano")
    else:
        print(f"Es Americano y de {ciudad}")
else:
    print(f"{nombre} no es mayor de edad")

# Ejemplo 4

print("\n#################### EJEMPLO 4 ####################")

#dia = int(input("Escriba un numero: "))
dia = 1
if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
else:
    print("Es fin de semana!")


# Ejemplo 5

print("\n#################### EJEMPLO 5 ####################")

edad_minima = 18
edad_maxima = 65
edad_oficial = 65

if edad_oficial >= 18 and edad_oficial <= edad_maxima:
    print("Esta en edad de Trabajar!!")
else:
    print("No está en edad de trabajar")

# Ejemplo 6

print("\n#################### EJEMPLO 6 ####################")

pais = "Alemania"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana!")
else:
    print("{} NO es un pais de habla hispana".format(pais))

# Ejemplo 7

print("\n#################### EJEMPLO 7 ####################")

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un pais de habla hispana!")
else:
    print("{} SI es un pais de habla hispana".format(pais))


# Ejemplo 8

print("\n#################### EJEMPLO 8 ####################")

pais = "EUA"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es un pais de habla hispana!")
else:
    print("{} SI es un pais de habla hispana".format(pais))
