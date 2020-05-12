# -*- coding: utf-8 -*-

# Ejemplo de condicionales: (Número primo)

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n > 2 and n % 2 == 0:
        return False
    else:
        for i in range(3,n):
            if n % i == 0:
                return False
        return True

def main():

    print('')
    n = int(input('Digite su número: '))
    result = is_prime(n)

    if result is True:
        print('')
        print('Su número es primo')
    else:
        print('')
        print('Su número no es primo')

if __name__ == '__main__':
    main()


# CONDICIONALES: 
# - Una expresión booleana se evalúa como verdadera o fals (True, False)
# - Operadores relacionales: ==, !=, >, >=, <, <=
# - Operadores logicos: and, or not --> Sigue la logica matemática

# Pass debajo de una función para que no haga nada 

# PARA INGRESAR  AL ZEN DE PYTHON USO --> import this
