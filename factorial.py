# -*- coding: utf-8 -*-

def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n-1)

if __name__ == '__main__':

    print('')
    n = int(input('Digite su número: '))

    result = factorial(n)

    print('')
    print(result)
