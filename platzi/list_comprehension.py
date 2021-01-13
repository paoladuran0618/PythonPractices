# -*- coding: utf-8 -*-

def sin_list_comprehension():
    pares = []
    for num in range(1,31):
        if num % 2 == 0:
            pares.append(num)
    print(pares)

if __name__ == '__main__':
    sin_list_comprehension()
    #with list comprehension
    even = [num for num in range(1,31) if num % 2 == 0]
    print(even)