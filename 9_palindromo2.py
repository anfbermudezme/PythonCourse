
# Código para reconocer palabras palindromas además del uso de loops y condicionales

def palindromo2(palabra):

    palabra_inversa = palabra[::-1]

    if palabra == palabra_inversa:
        return True

    return False


if __name__ == '__main__':

    print('')
    palabra = str(input('Ingrese su palabra: '))

    result = palindromo2(palabra)

    if result is True:
        print('{} es palíndromo.'.format(palabra))
    else:
       print('{} no es palindromo.'.format(palabra))
