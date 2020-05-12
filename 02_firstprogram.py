# -*- coding: utf-8 -*-

#Para hacer el triangulo es primero graficar una linea, dar vuelta 120 grados y así 3 veces 

import turtle

window =  turtle.Screen()
triangulo = turtle.Turtle ()
triangulo.forward(350)
triangulo.left(120)
triangulo.forward(350)
triangulo.left(120)
triangulo.forward(350)


turtle.mainloop()  #mainloop() s para que no se me cierre la ventana

#Para ejecutar un programa abro el cmd en windows o terminal en mac y se escribe "python ejemplo.py"


#Para salir de python en cmd o terminal pongo --> exit()

#Operadores: 

# + , - , * , / , // , % , ** , > , < , == , >= , <=

# Ejemplo de operador: 

#  5/4 : 1.25 , 5//4 : 1--> Acá se pierde información 

#Orden de operaciones: 

#PEMDAS: Parentesis, exponntes, mult/divi, Adición/Sustracción

#Valores: Letra o número

#los tipos básicos son: Integer <int>, Float <float>, String<str>, Boolean<bool>

#Para ver que tipo de valor es: --> type()

# Continuo en 4_
