# encoding:utf-8

###################################################
# Primitivas de Diseño                            #
# Por Alvaro Sacari Alanoca                       #
# para el curso de CAD, Ing. Edwin Hinojosa Ramos #
###################################################

######################################
# la librería turtle depende de TK   #
# instale el siguiente paquete para  #
# poder correr la aplicación :)      #
#                                    #
# $sudo apt-get install python-tk    #
######################################
import turtle


def pintar(x, y):
    ##################################
    # Función para Encender un Pixel #
    ##################################
    turtle.delay(0)
    turtle.speed(0)
    turtle.ht()
    turtle.up()
    turtle.goto(2 * int(x), 2 * int(y))
    turtle.down()
    turtle.fd(0)
    turtle.up()



