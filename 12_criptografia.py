# -*- coding: utf-8 -*- 

# Este programa es un ejemplo de Keys s identifican por estar detro de {} y además tener un {key:value}
# Buscar en la documentación de python todos los metodos de Keys 

Keys = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': ';',
    'k': 'z',
    'l': '8',
    'm': 'm',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y', 
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': '!',
    'z': 'W', 
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',    
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',  
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l', 
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K', 
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B', 
    
}

def cypher(message):

 #Split convierte un string en una lista
    words = message.split(' ')

    cypher_message = []

    for word in words:
        cypher_word = ''
        for letter in word:
            cypher_word += Keys[letter]

        cypher_message.append(cypher_word)

# Append nos agrega nuevos elementos a una lista

    return ' '.join(cypher_message)    

# Join sirve para convertir una lista en un string

def decypher(message):
    words =message.split()

    decypher_message = []

    for word in words: 
        decypher_word = ''
        for letter in word: 

            for key, value in Keys.items():
                if value == letter:
                    decypher_word += key

        decypher_message.append(decypher_word)        

    return ' '.join(decypher_message)                 
                 
def run():

    while True: 

        command = str(input('''___*___*___*___*___*___*___*___*___*___*___*___*___*___*___*___*___*___*___
            Bienvenido a criptografía. Escoge una opción: 
            [c]ifrar mensaje
            [d]escifrar mensaje
            [s]alir
        ''')) 

        if command == 'c':
            message = str(input('Escribe tu mensaje: '))
            cypher_message = cypher(message)
            print(' ')
            print(cypher_message)
            print(' ')
        elif command == 'd': 
            message = str(input('Escribe tu mensaje encriptado: '))
            decypher_message = decypher(message)
            print(' ')
            print(decypher_message)
            print(' ')
        elif command == 's':
            return exit() 
        else: 
            print('No seleccionó ninguna opción')           

if __name__ == '__main__': 
    print ('Mensajes cifrados')
    run()