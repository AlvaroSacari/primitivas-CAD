# encoding:utf-8
__author__ = 'alvaro'

import math

import pixel


def pintar_simetria(a, b, xc, yc):
    pixel.pintar(a + xc, b + yc)
    pixel.pintar(-a + xc, b + yc)
    pixel.pintar(a + xc, -b + yc)
    pixel.pintar(-a + xc, -b + yc)
    pixel.pintar(b + xc, a + yc)
    pixel.pintar(-b + xc, a + yc)
    pixel.pintar(b + xc, -a + yc)
    pixel.pintar(-b + xc, -a + yc)


def bresenham(xc, yc, radio):
    ########################################################
    # el algoritmo se efectúa en un sector circular de 45° #
    ########################################################

    # para pintar el centro de la circunferencia

    # pixel.pintar(xc, yc)

    xi = 0
    xf = int(round(radio / math.sqrt(2)))
    yi = radio

    print('xf : {}'.format(xf))
    print('yi : {}'.format(yi))

    for i in range(0, xf + 1):
        da = yi ** 2 + xi ** 2 - radio ** 2
        db = (yi - 1) ** 2 + xi ** 2 - radio ** 2

        if da == 0:
            pintar_simetria(xi, yi, xc, yc)
        elif db == 0:
            pintar_simetria(xi, yi - 1, xc, yc)

        s = da + db

        if s > 0:
            pintar_simetria(xi + 1, yi - 1, xc, yc)
            xi, yi = xi + 1, yi - 1
        else:
            pintar_simetria(xi + 1, yi, xc, yc)
            xi, yi = xi + 1, yi

"""
pixel.ejes()
bresenham(-40, -30, 30)

a = raw_input('enter ..')
"""