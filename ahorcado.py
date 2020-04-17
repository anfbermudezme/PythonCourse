# -*- coding: utf-8 -*-

import random

IMAGES = ['''
    
    *-----*
    |     |
          |
          |
          |
          |
          |
          |
          ========''', '''

    *-----*
    |     |
    0     |
          |
          |
          |
          |
          |
          ========''','''
    
    *-----*
    |     |
    0     |
    |     |
          |
          |
          |
          |
          ========''','''

    *-----*
    |     |
    0     |
   /|     |
          |
          |
          |
          |
          ========''','''

    *-----*
    |     |
    0     |
   /|\    |
          |
          |
          |
          |
          ========''','''

    *-----*
    |     |
    0     |
   /|\    |
    |     |
          |
          |
          |
          ========''','''

    *-----*
    |     |
    0     |
   /|\    |
    |     |
   /      |
          |
          |
          ========''','''

    *-----*
    |     |
    0     |
   /|\    |
    |     |
   / \    |
          |
          |
          ========''','''      
'''    
]


WORDS = ['amor', 'estudio', 'celular', 'lampara', 'esfero', 'marcador', 'resaltador', 'libros','computador','agua','cuaderno','modem','guitarra','televisor','tablero']

def random_WORD():
    indice = random.randint(0, len(WORDS) - 1)
    return WORDS[indice]

def muestra_board(hidden_WORD, intentos):
    print('_____________________________________________________________________________')
    print('')
    print (IMAGES[intentos])
    print('')
    print (hidden_WORD)
    print('')
    print('')
    print('')
    print('_____________________________________________________________________________')

def run():
    word = random_WORD()
    hidden_WORD =['_'] * len(word)
    intentos = 0
    
    while True: 
        muestra_board(hidden_WORD, intentos)
        print('')
        escoger_letra = str(input('Escoge una letra:  '))

        letra_indices = []
        for i in range(len(word)):
            if word[i] == escoger_letra:
                letra_indices.append(i)
        
        if  len(letra_indices) == 0:
             intentos += 1 

             if intentos == 7:
                 muestra_board(hidden_WORD,intentos)
                 print('')
                 print('PERDISTE! La palabra correcta era: {}'.format(word))
                 print('_____________________________________________________________________________')
                 print('')
                 break 

        else: 
            for i in letra_indices:
                hidden_WORD[i] = escoger_letra

            letra_indices = []
        try:
          hidden_WORD.index('_')   
        except ValueError:
            print('_____________________________________________________________________________')
            print('')
            print('FELICIDADES GANASTE ! La palabra es: {}'.format(word))
            print('_____________________________________________________________________________')
            print('')
            break                 


if __name__ == '__main__':
    print('')
    print('')
    print('ESTE ES EL JUEGO DE AHORCADO, BIENVENIDO')
    run()

