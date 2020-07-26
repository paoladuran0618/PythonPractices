"""Realiza un programa que pida al usuario cuantos números 
quiere introducir. Luego lee todos los números y realiza 
una media aritmética."""

n = int( input("Cuantos numeros quiere introducir? ") )
i = 0
suma = 0
print("Introduzca los numeros: ")
while i < n:
    suma += float( input() )
    i+=1

print("La media es: ", suma / n)
