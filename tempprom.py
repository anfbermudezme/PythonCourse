# -*- coding: utf-8 -*-

def p_temps(temperaturas):

    sum_of_temps = 0

    for temperatura in temperaturas:

# En python 3 no es necesario  declarar el float

        sum_of_temps += float(temperatura)

    return sum_of_temps / len(temperaturas)



if __name__ == '__main__':
    temperaturas = [21, 19, 18, 24, 32, 17, 19, 24]

# Primero declarar que función vamos a definir.

    result= p_temps(temperaturas)

    print('La temperatura promedio es: {}'.format(result))
