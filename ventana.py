__author__ = 'alvaro'
import turtle


def mantener():
    turtle.mainloop()

def titulo(cad):
    turtle.title(cad)

def limpiar():
    turtle.clearscreen()
    ejes()


def ejes():
    ####################################
    # Ejes Coordenados                 #
    # los ejes x e y van de -150 a 150 #
    ####################################
    turtle.delay(0)
    turtle.ht()
    turtle.speed(0)
    turtle.pencolor('red')
    turtle.down()
    turtle.fd(301)
    turtle.rt(90)
    turtle.fd(1)
    turtle.rt(90)
    turtle.fd(300)
    turtle.lt(90)
    turtle.fd(300)
    turtle.rt(90)
    turtle.fd(1)
    turtle.rt(90)
    turtle.fd(300)
    turtle.lt(90)
    turtle.fd(300)
    turtle.rt(90)
    turtle.fd(1)
    turtle.rt(90)
    turtle.fd(300)
    turtle.lt(90)
    turtle.fd(300)
    turtle.rt(90)
    turtle.fd(1)
    turtle.rt(90)
    turtle.fd(300)
    turtle.up()
    turtle.pencolor('blue')

