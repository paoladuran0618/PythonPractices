n1 = float( input("introduzca el primer numero: ") )
n2 = float( input("introduzca el segundo numero: ") )

print("Menú")
print("Opción 1: Mostrar suma de ambos números. ")
print("Opción 2: Mostrar resta de los números. ")
print("Opción 3: Mostrar multiplicación de los dos números. \n")
opcion = int ( input ("Introduzca la opción (sólo números enteros del 1 al 3). ") )

if opcion >=1 and opcion <=3:
    if opcion == 1:
        print("La suma es: ", n1 + n2)
    elif opcion == 2:
        print("La resta es: ", n1 - n2)
    else:
        print("La multiplicación es: ", n1 * n2)
else:
    print("Introdujo un número incorrecto.")
