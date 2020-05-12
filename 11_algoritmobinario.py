# -*- coding: utf-8 -*-

# Este es el primer algoritmo que haré

def binary_search(numeros, numero_find, low, high):
    
    if low > high:
        return False

# ESTE PROGRAMA SIRVE PARA PYTHON2 SIN HACER USO DEL INT, SE USA EL INT PARA QUE FUNCIONE EN PYTHON3

    mid = int((low + high) / 2)

    if numeros[mid] == numero_find:
        return True

    elif numeros[mid] > numero_find:
        return binary_search(numeros, numero_find, low, mid - 1)
    else:
        return binary_search(numeros, numero_find, mid + 1, high)    



if __name__ == '__main__':

    numeros = [1,3,4,5,6,7,8,9,11,23,45,67,78,83,86,90,98,103,105,176,627,1627]

    numero_find = int(input('ingresa un número: '))

    result = binary_search (numeros, numero_find, 0, len(numeros) - 1)

    if result is True:
        print('Número encontrado, es {} y si esta en la lista.'.format(numero_find))
    else:
        print('El número no esta en la lista.')    

