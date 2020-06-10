""""
Variables en Python

"""

texto = "Master en Python"
texto2 = "Con ese man"
print(texto)
print(texto2)

print("------------------------------------------")

# Concatenación

nombre = "Eduardo"
apellidos = "Onofre"
web = "EdOweb.mx"

print(nombre + " " + apellidos + "-" + web)
print(f"{nombre} {apellidos} - {web}") #INTERPOLACION la f me deja formatear dentro de un texto una variable
print("Hola me llamo {} {} y mi web es: {}".format(nombre,apellidos,web))
