# -*- coding: utf-8 -*-


#EJEMPLO IMPORTANTE DE FUNCIÓN SIGUIENDO DE 2_firstprogram.py

import turtle

def main():
    window = turtle.Screen()
    cuadrado = turtle.Turtle()
    make_square(cuadrado)
    turtle.mainloop()

def make_square(cuadrado):
    lenght= int(input('Tamaño de cuadrado: '))

    for i in range (4):
        make_line_and_turn(cuadrado, lenght)

def make_line_and_turn(cuadrado, length):
    cuadrado.forward(length)
    cuadrado.left(90)

if __name__ == '__main__':  # En python siempre debemos ponerlo, "Las funciones se definen encima de esto"
    main()

# FUNCIONES: 

# - Una función es una secuencia de comandos que realizan un cómputo
# - Para definirla se usa el keyword "def", se le asigna un nombre y se define la secuencia de comandos
# - Las funciones son llamadas por su nombr y regresan su "result"
# - Pueden recibir 0 o más parametros

# EJEMPLO def suma(num1, num2): return num1 + num 2 

# Limites para funciones: 
# - No pude empezar el nombre con un dígito
# - No puede ser una palabra reservada como lo vimos en 3_
# - Variables y funciones deben llamarse diferente
