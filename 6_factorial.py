# -*- coding: utf-8 -*-

# Ejemplo de función recursiva: (Factorial)

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

# DOCUMENTACIÓN DE PYTHON : python.org

# Un string no se puede modificar

# Funciones de recursión: Función que se ejecuta dentro de si misma