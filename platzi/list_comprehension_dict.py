#Listas de comprensión con diccionarios

# -*- coding: utf-8 -*-

def cuadrado():
    cuadrados = {}
    for num in range(1, 11):
        cuadrados[num] = num**2
    print(cuadrados)

if __name__ == '__main__':
    cuadrado()
    #sin listas de comprension
    squares = {num: num**2 for num in range(1, 11)}
    print(squares)
