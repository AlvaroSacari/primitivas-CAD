# encoding:utf-8
import pixel

__author__ = 'alvaro'


def metodo_directo(xi, yi, xf, yf):
    ####################################
    # Trazado de líneas METODO DIRECTO #
    ####################################
    # si se trata de una linea horizontal
    if yi == yf and xi != xf:
        if xi < xf:
            pass
        elif xi > xf:
            aux = xi
            xi = xf
            xf = aux
        for i in range(xi, xf + 1):
            pixel.pintar(i, yi)

    # si se trata de una linea vertical
    elif xi == xf and yi != yf:
        if yi > yf:
            aux = yi
            yi = yf
            yf = aux
        elif yi < yf:
            pass
        for i in range(yi, yf + 1):
            pixel.pintar(xi, i)

    # si se trata de una linea diagonal
    elif xf - xi == yf - yi:
        h = int(0)
        if xi < xf:
            pass
        elif xi > xf:
            xi, yi, xf, yf = xf, yf, xi, yi

        for i in range(xi, xf + 1):
            pixel.pintar(i, yi + h)
            h += 1

    elif xf - xi == -(yf - yi):
        h = int(0)
        if xi > xf:
            xi, yi, xf, yf = xf, yf, xi, yi


        elif xi < xf:
            pass
        for i in range(xi, xf + 1):
            pixel.pintar(i, yi - h)
            h += 1

            # si se trata de una linea arbitraria
            #
            #


def add_simple(xi, yi, xf, yf):
    #######################################
    # Trazado de líneas METODO ADD SIMPLE #
    #######################################
    m = float((yf - yi) / (xf - xi))
    if (abs(m) < 1 and xi > xf) or (abs(m) > 1 and yf < yi):
        # intercambiar (xi,yi) y (xf,yf)
        aux = xi
        xi = xf
        xf = aux
        auy = yi
        yi = yf
        yf = auy
    else:
        pass
    pixel.pintar(xi, yi)
    if abs(m) < 1:
        yc = float(yi)
        for h in range(xi + 1, xf - 1 + 1):
            yc += m
            ryc = int(round(yc))
            pixel.pintar(h, ryc)
        pixel.pintar(xf, yf)
    else:
        if abs(m) > 1:
            im = float(1.0 / m)
            xc = float(xi)
            for h in range(yi + 1, yf - 1 + 1):
                xc += im
                rxc = round(xc)
                pixel.pintar(rxc, h)
            pixel.pintar(xf, yf)
        else:
            pass


def add_entero(xi, yi, xf, yf):
    if xi > xf or yi > yf:
        xi, yi, xf, yf = xf, yf, xi, yi

    # para el caso 3 :
    if xf - xi != 0:
        m = float(yf - yi) / float(xf - xi)
        if -1 < m < 0 or m < -1:
            if xi < xf:
                xi, yi, xf, yf = xf, yf, xi, yi
    else:
        # se trata de una línea vertical
        xant = xi
        yant = yi
        while xant != xf or yant != yf:
            ysig = yant + 1
            pixel.pintar(xant, ysig)
            yant = ysig

    print(xi, yi)
    print(xf, yf)
    #######################################
    # Trazado de líneas METODO ADD ENTERO #
    #######################################
    dx = xf - xi
    dy = yf - yi

    xant = xi
    yant = yi

    error = 0

    pixel.pintar(xi, yi)

    if dx != 0:
        m = float(dy) / float(dx)

    else:
        # se trata de una línea vertical
        while xant != xf or yant != yf:
            ysig = yant + 1
            pixel.pintar(xant, ysig)
            yant = ysig

    while xant != xf or yant != yf:
        # PRIMER CASO
        if 0 < m < 1 and (dx > 0 and dy > 0):
            if error < 0:
                xsig = xant + 1
                ysig = yant
                error += dy
            else:
                xsig = xant + 1
                ysig = yant + 1
                error += (dy - dx)
            pixel.pintar(xsig, ysig)
            xant = xsig
            yant = ysig

        # SEGUNDO CASO
        elif m > 1 and (dx >= 0 and dy >= 0):

            if error < 0:
                xsig = xant + 1
                ysig = yant + 1
                error = error + (dy - dx)
            else:
                xsig = xant
                ysig = yant + 1
                error = error - dx
            pixel.pintar(xsig, ysig)
            xant = xsig
            yant = ysig

        # TERCER CASO
        elif -1 < m < 0 and (dx < 0 <= dy):

            if error < 0:
                xsig = xant - 1
                ysig = yant
                error = error + dy
            else:
                xsig = xant - 1
                ysig = yant + 1
                error = error + (dx + dy)
            pixel.pintar(xsig, ysig)
            xant = xsig
            yant = ysig

        # CUARTO CASO
        elif m < -1 and (dx < 0 <= dy):

            if error < 0:
                xsig = xant - 1
                ysig = yant + 1
                error = error + (dx + dy)
            else:
                xsig = xant
                ysig = yant + 1
                error = error + dx
            pixel.pintar(xsig, ysig)
            xant = xsig
            yant = ysig

        # Caso de una línea horizontal
        elif dy == 0:
            xsig = xant + 1
            pixel.pintar(xsig, yant)
            xant = xsig

        # caso de una línea diagonal
        elif xf - xi == yf - yi:
            xsig = xant + 1
            ysig = yant + 1
            pixel.pintar(xsig, ysig)
            xant = xsig
            yant = ysig
        elif xf - xi == -(yf - yi):
            if xi < xf:
                xsig = xant + 1
                ysig = yant - 1
                pixel.pintar(xsig, ysig)
                xant = xsig
                yant = ysig
            else:
                xsig = xant - 1
                ysig = yant + 1
                pixel.pintar(xsig, ysig)
                xant = xsig
                yant = ysig