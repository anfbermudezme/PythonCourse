# -*- coding: utf-8 -*-

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

if __name__ == '__main__':
    main()
