__author__ = 'alvaro'

import linea


def triangulo(x1, y1, x2, y2, x3, y3):
    linea.add_entero(x1, y1, x2, y2)
    linea.add_entero(x2, y2, x3, y3)
    linea.add_entero(x1, y1, x3, y3)


def rectangulo(x1, y1, x2, y2):
    gx1 = x1
    gy1 = y1
    gx2 = x2
    gy2 = y1
    gx3 = x2
    gy3 = y2
    gx4 = x1
    gy4 = y2
    linea.add_entero(gx1, gy1, gx2, gy2)
    linea.add_entero(gx2, gy2, gx3, gy3)
    linea.add_entero(gx3, gy3, gx4, gy4)
    linea.add_entero(gx1, gy1, gx4, gy4)


def rectangulo_4p(x1, y1, x2, y2, x3, y3, x4, y4):
    gx1 = x1
    gy1 = y1
    gx2 = x3
    gy2 = y3
    gx3 = x2
    gy3 = y2
    gx4 = x4
    gy4 = y4
    linea.add_entero(gx1, gy1, gx2, gy2)
    linea.add_entero(gx2, gy2, gx3, gy3)
    linea.add_entero(gx3, gy3, gx4, gy4)
    linea.add_entero(gx1, gy1, gx4, gy4)