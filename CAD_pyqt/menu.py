# encoding:utf-8

import linea

def menu():
    ##################
    # Menú Principal #
    ##################
    # print '\n[1] Trazado de Líneas - METODO DIRECTO'
    # print '[2] Trazado de Líneas - METODO ADD SIMPLE'
    print '\n[3] Línea - ADD Entero'
    print '[4] Circunferencia - Bresenham\n'

    print '[10] limpiar plano'
    print '[11] Salir\n'

    opcion = raw_input('opción : ')

    if opcion == '1':
        xi = int(raw_input('xi : '))
        yi = int(raw_input('yi : '))
        xf = int(raw_input('xf : '))
        yf = int(raw_input('yf : '))
        linea.metodo_directo(xi, yi, xf, yf)

    elif opcion == '2':
        xi = int(raw_input('xi : '))
        yi = int(raw_input('yi : '))
        xf = int(raw_input('xf : '))
        yf = int(raw_input('yf : '))
        linea.add_simple(xi, yi, xf, yf)

    elif opcion == '3':
        xi = int(raw_input('xi : '))
        yi = int(raw_input('yi : '))
        xf = int(raw_input('xf : '))
        yf = int(raw_input('yf : '))
        linea.add_entero(xi, yi, xf, yf)

    elif opcion == '4':
        xc = int(raw_input('xc : '))
        yc = int(raw_input('yc : '))
        radio = int(raw_input('radio : '))
        circunferencia.bresenham(xc, yc, radio)


    elif opcion == '10':
        pixel.limpiar()
        menu()

    elif opcion == '11':
        print '\nGracias :)'
        return None
