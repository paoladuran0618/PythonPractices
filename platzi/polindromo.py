# -*- coding: utf-8 -*-

def run():
    word = str(input('Introduce la palabra: '))
    if word == word[::-1]:
        print("La palabra es un políndromo.")
    else:
        print('No es un polindromo')

if __name__ == '__main__':
    run()