# -*- coding: utf-8 -*-

# Código para reconocer palabras palindromas además del uso de loops y condicionales

def palindrome(w):

    reverse_letters = []

    for letter in w:
        reverse_letters.insert(0,letter)

    reverse_w = ''.join(reverse_letters)

    if reverse_w == w:
        return True

    return False

if __name__ == '__main__':
    w = str(input('Escribe una palabra: '))

    result = palindrome(w)

    if result is True:
        print('{} es palíndromo.'.format(w))
    else:
        print('{} no es palíndromo.'.format(w))
