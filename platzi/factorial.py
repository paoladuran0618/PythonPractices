# -*- coding: utf-8 -*-


def factorial(num):
    if num == 0:
        return 1

    return num * factorial(num - 1)


if __name__ == '__main__':
    number = int(input('Escribe un numero: '))

    result = factorial(number)
    print(result)