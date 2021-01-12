# -*- coding: utf-8 -*-

from random import sample

def binary_search(random_list, number_to_find, low, high):
    if low > high:
        return False
    
    mid = int((low + high)/2)

    if random_list[mid] == number_to_find:
        return True
    elif random_list[mid] > number_to_find:
        return binary_search(random_list, number_to_find, low, mid -1)
    else:
        return binary_search(random_list, number_to_find, mid + 1, high)

if __name__ == '__main__':
    random_list = sample(range(0,200), 200)
    random_list.sort()
    number_to_find = int(input('Ingresa el número que quieres buscar: '))

    result = binary_search(random_list, number_to_find, 0, len(random_list)-1)
    if result is True:
        print('El numero si esta en la lista.')
    else:
        print('El numero no está en la lista.')