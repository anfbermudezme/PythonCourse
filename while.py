# -*- coding: UTF-8 -*-

import random


def run():
    n_found = False
    random_n = random.randint(0, 20)

    while not n_found:
        print('')

        n = int(input('Intente un número:  '))

        if n == random_n:
            print ('')
            print ('Felicidades!')
            n_found = True
        elif n > random_n:
            print('')
            print('El número es más pequeño')
        else:
            print('')
            print('El número es más grande')

if __name__ == '__main__':
    run()
