""" Realiza un programa que lea un número impar por teclado. Si el usuario 
no introduce un número impar, debe repetise el proceso hasta que 
lo introduzca correctamente. """

n1 = int( input("introduzca un número (debe ser impar). ") )

while n1 % 2 == 0:
    n1 = int( input("El número debe ser impar, vuelve a introducirlo. ") )
else:
    print("El numero es impar :) ")
