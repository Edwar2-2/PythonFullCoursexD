""""
Ejercicio 2. 
Escribir un script que muestre todos los numeros pares del 1 al 120


"""



while contador <= 120:

    print(contador)
    contador += 2

print("-------- USANDO FOR ------")

for contador in range(1, 121):
    if contador%2 == 0: # Si su residuo es igual a 0 entonces es par
        print(contador)