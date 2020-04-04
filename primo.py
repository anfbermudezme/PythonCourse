# -*- coding: utf-8 -*-

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
            else:
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
