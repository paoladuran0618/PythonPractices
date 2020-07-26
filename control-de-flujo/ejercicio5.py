""" Realiza un programa que pida al usuario un número entero del 0 al 9, 
y que mientras el número no sea correcto se repita el proceso. Luego debe 
comprobar si el número se encuentra en la lista de números y notificarlo"""

numeros = [1, 5, 9, 4]

while True:
    numero = int( input("Introduzca el numero: ") )
    if numero >= 0 and numero <= 9:
        break
if numero in numeros:
    print("El numero esta dentro de la lista")
else:
    print("El numero no se encuentra en la lista")

    

