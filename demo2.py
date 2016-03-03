__author__ = 'alvaro'

import turtle
import linea
import figura
import ventana


def fondo_demo():
    turtle.pencolor('black')


def rayo(x):
    linea.add_entero(x, 10, x, 50)


def avion(a, b, salto):
    for i in range(a, b, salto):
        turtle.clearscreen()
        x1 = i
        x2 = i - 3
        x3 = i + 3
        figura.triangulo(x1, 7, x2, 0, x3, 0)
        turtle.pencolor('red')
        rayo(x1)
    avion(b, a, -salto)

##########
# INICIO #
##########
ventana.titulo('Alvaro DEMO')
fondo_demo()
avion(-20, 20, 2)
ventana.mantener()
