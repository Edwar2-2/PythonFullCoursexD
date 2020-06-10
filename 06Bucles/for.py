"""
# FOR

for variable in elemento_iterable(lista, rango, tupla, diccionario, etc):
    Bloque de instrucciones


"""
contador = 0
resultado = 0
for contador in range(0,10):
    print(f"Voy por el {contador}")

    resultado += contador

print("El resultado es: {}".format(resultado))


# Ejemplo tablas de multiplicar
print("\n ####################### EJEMPLO ###################")

numero_usuario = int(input("Escribe la tabla que quieres ver: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"\n----- Tabla de multiplicar del numero {numero_usuario} -----")

for numero_tabla in range(1,11):

    if numero_usuario == 45:
        print("Numero no permitido!")
        break

    print(f"{numero_usuario} x {numero_tabla} = {numero_tabla*numero_usuario}")
else:
    print("Tabla finalizada.")   