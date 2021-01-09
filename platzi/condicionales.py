# -*- coding: utf-8 -*-

def say_hello(age):
    if age > 20:
        print('Hola señor.')
    else:
        print('Hola niño')

if __name__ == "__main__":
    age = input('Ingrese su edad: ')
    say_hello(age)