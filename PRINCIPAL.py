# encoding:utf-8
__author__ = 'alvaro'

import curva
import linea
import circunferencia
import ventana
import figura
import transformacion


def separar_puntos(punto):
    aux = punto.split(' ')
    return int(aux[0]), int(aux[1])


def menu_trans():
    ############################
    # MENU DE TRANSFORMACIONES #
    ############################
    print('figuras : {}'.format(l_figura))

    print('\n\t[1] Traslación')
    print('\t[2] Rotación')
    print('\t[3] Escalamiento')
    print('\t[4] Afilamiento X')
    print('\t[5] Afilamiento Y')
    print('\t[6] Reflexión al eje  X')
    print('\t[7] Reflexión al eje Y')
    print('\t[8] Reflexión a Y = X')
    print('\t[9] Reflexión a Y = -X')
    print('\t[10] Return')

    opcion = raw_input('\n\topción : ')

    if opcion == '1': # Traslación
        q_fig = raw_input('\n\t¿Que figura desea trasladar?')
        tx = int(raw_input('\tDesplazamiento horizontal : '))
        ty = int(raw_input('\tDesplazamiento vertical : '))
        lista_aux = []
        if q_fig == 'linea':
            aux = l_figura.index('linea')
            lista_aux = transformacion.traslacion([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4]], tx, ty)

            # ventana.limpiar()

            linea.add_entero(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]

        elif q_fig == 'circunferencia':

            aux = l_figura.index('circunferencia')
            lista_aux = transformacion.traslacion([l_figura[aux + 1], l_figura[aux + 2]], tx, ty)

            # ventana.limpiar()

            circunferencia.bresenham(lista_aux[0], lista_aux[1], l_figura[aux + 3])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]

        elif q_fig == 'triangulo':

            aux = l_figura.index('triangulo')
            lista_aux = transformacion.traslacion([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4], l_figura[aux + 5], l_figura[aux + 6]], tx, ty)

            # ventana.limpiar()

            figura.triangulo(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3], lista_aux[4], lista_aux[5])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]
            l_figura[aux + 5] = lista_aux[4]
            l_figura[aux + 6] = lista_aux[5]

        elif q_fig == 'rectangulo':

            aux = l_figura.index('rectangulo')
            lista_aux = transformacion.traslacion([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4]], tx, ty)

            # ventana.limpiar()

            figura.rectangulo(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]

        elif q_fig == 'bezier':

            aux = l_figura.index('bezier')
            lista_aux = transformacion.traslacion([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4], l_figura[aux + 5], l_figura[aux + 6], l_figura[aux + 7], l_figura[aux + 8]], tx, ty)

            #ventana.limpiar()

            curva.bezier(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3], lista_aux[4], lista_aux[5], lista_aux[6], lista_aux[7])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]
            l_figura[aux + 5] = lista_aux[4]
            l_figura[aux + 6] = lista_aux[5]
            l_figura[aux + 7] = lista_aux[6]
            l_figura[aux + 8] = lista_aux[7]


        menu_trans()

    elif opcion == '2': # Rotación
        q_fig = raw_input('\n\t¿Que figura desea rotar?')
        tita = int(raw_input('\tángulo : '))
        lista_aux = []
        if q_fig == 'linea':
            aux = l_figura.index('linea')
            lista_aux = transformacion.rotacion([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4]], tita)

            # ventana.limpiar()

            linea.add_entero(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]

        elif q_fig == 'circunferencia':

            aux = l_figura.index('circunferencia')
            lista_aux = transformacion.rotacion([l_figura[aux + 1], l_figura[aux + 2]], tita)

            # ventana.limpiar()

            circunferencia.bresenham(lista_aux[0], lista_aux[1], l_figura[aux + 3])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]

        elif q_fig == 'triangulo':

            aux = l_figura.index('triangulo')
            lista_aux = transformacion.rotacion([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4], l_figura[aux + 5], l_figura[aux + 6]], tita)

            # ventana.limpiar()

            figura.triangulo(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3], lista_aux[4], lista_aux[5])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]
            l_figura[aux + 5] = lista_aux[4]
            l_figura[aux + 6] = lista_aux[5]

        elif q_fig == 'rectangulo':

            aux = l_figura.index('rectangulo')
            lista_aux = transformacion.rotacion([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4]], tita)

            # ventana.limpiar()

            figura.rectangulo(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]

        elif q_fig == 'bezier':

            aux = l_figura.index('bezier')
            lista_aux = transformacion.rotacion([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4], l_figura[aux + 5], l_figura[aux + 6], l_figura[aux + 7], l_figura[aux + 8]], tita)

            #ventana.limpiar()

            curva.bezier(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3], lista_aux[4], lista_aux[5], lista_aux[6], lista_aux[7])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]
            l_figura[aux + 5] = lista_aux[4]
            l_figura[aux + 6] = lista_aux[5]
            l_figura[aux + 7] = lista_aux[6]
            l_figura[aux + 8] = lista_aux[7]

        menu_trans()

    elif opcion == '3': # Escalamiento
        q_fig = raw_input('\n\t¿Que figura desea escalar?')
        ex = int(raw_input('\tEscalamiento en X : '))
        ey = int(raw_input('\tEscalamiento en Y : '))
        lista_aux = []
        if q_fig == 'linea':
            aux = l_figura.index('linea')
            lista_aux = transformacion.escalamiento([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4]], ex, ey)

            # ventana.limpiar()

            linea.add_entero(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]

        elif q_fig == 'circunferencia':

            aux = l_figura.index('circunferencia')
            lista_aux = transformacion.escalamiento([l_figura[aux + 1], l_figura[aux + 2]], ex, ey)

            # ventana.limpiar()

            circunferencia.bresenham(lista_aux[0], lista_aux[1], l_figura[aux + 3])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]

        elif q_fig == 'triangulo':

            aux = l_figura.index('triangulo')
            lista_aux = transformacion.escalamiento([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4], l_figura[aux + 5], l_figura[aux + 6]], ex, ey)

            # ventana.limpiar()

            figura.triangulo(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3], lista_aux[4], lista_aux[5])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]
            l_figura[aux + 5] = lista_aux[4]
            l_figura[aux + 6] = lista_aux[5]

        elif q_fig == 'rectangulo':

            aux = l_figura.index('rectangulo')
            lista_aux = transformacion.escalamiento([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4]], ex, ey)

            # ventana.limpiar()

            figura.rectangulo(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]

        elif q_fig == 'bezier':

            aux = l_figura.index('bezier')
            lista_aux = transformacion.escalamiento([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4], l_figura[aux + 5], l_figura[aux + 6], l_figura[aux + 7], l_figura[aux + 8]], ex, ey)

            #ventana.limpiar()

            curva.bezier(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3], lista_aux[4], lista_aux[5], lista_aux[6], lista_aux[7])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]
            l_figura[aux + 5] = lista_aux[4]
            l_figura[aux + 6] = lista_aux[5]
            l_figura[aux + 7] = lista_aux[6]
            l_figura[aux + 8] = lista_aux[7]

        menu_trans()

    elif opcion == '4': # Afilamiento X
        q_fig = raw_input('\n\t¿Que figura desea afilar en X?')
        afx = int(raw_input('\tFactor de afilamiento afx : '))
        lista_aux = []
        if q_fig == 'linea':
            aux = l_figura.index('linea')
            lista_aux = transformacion.afilamiento_x([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4]], afx)

            # ventana.limpiar()

            linea.add_entero(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]

        elif q_fig == 'circunferencia':

            aux = l_figura.index('circunferencia')
            lista_aux = transformacion.afilamiento_x([l_figura[aux + 1], l_figura[aux + 2]], afx)

            # ventana.limpiar()

            circunferencia.bresenham(lista_aux[0], lista_aux[1], l_figura[aux + 3])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]

        elif q_fig == 'triangulo':

            aux = l_figura.index('triangulo')
            lista_aux = transformacion.afilamiento_x([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4], l_figura[aux + 5], l_figura[aux + 6]], afx)

            # ventana.limpiar()

            figura.triangulo(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3], lista_aux[4], lista_aux[5])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]
            l_figura[aux + 5] = lista_aux[4]
            l_figura[aux + 6] = lista_aux[5]

        elif q_fig == 'rectangulo':

            aux = l_figura.index('rectangulo')
            lista_aux = transformacion.afilamiento_x([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4], l_figura[aux + 3], l_figura[aux + 2], l_figura[aux + 1], l_figura[aux + 4]], afx)

            # ventana.limpiar()

            figura.rectangulo_4p(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3], lista_aux[4], lista_aux[5], lista_aux[6], lista_aux[7])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]

        elif q_fig == 'bezier':

            aux = l_figura.index('bezier')
            lista_aux = transformacion.afilamiento_x([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4], l_figura[aux + 5], l_figura[aux + 6], l_figura[aux + 7], l_figura[aux + 8]], afx)

            #ventana.limpiar()

            curva.bezier(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3], lista_aux[4], lista_aux[5], lista_aux[6], lista_aux[7])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]
            l_figura[aux + 5] = lista_aux[4]
            l_figura[aux + 6] = lista_aux[5]
            l_figura[aux + 7] = lista_aux[6]
            l_figura[aux + 8] = lista_aux[7]

        menu_trans()

    elif opcion == '5': # Afilamiento Y
        q_fig = raw_input('\n\t¿Que figura desea afilar en X?')
        afy = int(raw_input('\tFactor de afilamiento afy : '))
        lista_aux = []
        if q_fig == 'linea':
            aux = l_figura.index('linea')
            lista_aux = transformacion.afilamiento_y([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4]], afy)

            # ventana.limpiar()

            linea.add_entero(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]

        elif q_fig == 'circunferencia':

            aux = l_figura.index('circunferencia')
            lista_aux = transformacion.afilamiento_y([l_figura[aux + 1], l_figura[aux + 2]], afy)

            # ventana.limpiar()

            circunferencia.bresenham(lista_aux[0], lista_aux[1], l_figura[aux + 3])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]

        elif q_fig == 'triangulo':

            aux = l_figura.index('triangulo')
            lista_aux = transformacion.afilamiento_y([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4], l_figura[aux + 5], l_figura[aux + 6]], afy)

            # ventana.limpiar()

            figura.triangulo(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3], lista_aux[4], lista_aux[5])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]
            l_figura[aux + 5] = lista_aux[4]
            l_figura[aux + 6] = lista_aux[5]

        elif q_fig == 'rectangulo':

            aux = l_figura.index('rectangulo')
            lista_aux = transformacion.afilamiento_y([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4], l_figura[aux + 3], l_figura[aux + 2], l_figura[aux + 1], l_figura[aux + 4]], afy)

            # ventana.limpiar()

            figura.rectangulo_4p(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3], lista_aux[4], lista_aux[5], lista_aux[6], lista_aux[7])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]

        elif q_fig == 'bezier':

            aux = l_figura.index('bezier')
            lista_aux = transformacion.afilamiento_y([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4], l_figura[aux + 5], l_figura[aux + 6], l_figura[aux + 7], l_figura[aux + 8]], afy)

            #ventana.limpiar()

            curva.bezier(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3], lista_aux[4], lista_aux[5], lista_aux[6], lista_aux[7])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]
            l_figura[aux + 5] = lista_aux[4]
            l_figura[aux + 6] = lista_aux[5]
            l_figura[aux + 7] = lista_aux[6]
            l_figura[aux + 8] = lista_aux[7]

        menu_trans()

    elif opcion == '6': # Reflexion al eje X
        q_fig = raw_input('\n\t¿Que figura desea reflejar en X?')
        lista_aux = []
        if q_fig == 'linea':
            aux = l_figura.index('linea')
            lista_aux = transformacion.relexion_x([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4]])

            # ventana.limpiar()

            linea.add_entero(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]

        elif q_fig == 'circunferencia':

            aux = l_figura.index('circunferencia')
            lista_aux = transformacion.relexion_x([l_figura[aux + 1], l_figura[aux + 2]])

            # ventana.limpiar()

            circunferencia.bresenham(lista_aux[0], lista_aux[1], l_figura[aux + 3])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]

        elif q_fig == 'triangulo':

            aux = l_figura.index('triangulo')
            lista_aux = transformacion.relexion_x([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4], l_figura[aux + 5], l_figura[aux + 6]])

            # ventana.limpiar()

            figura.triangulo(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3], lista_aux[4], lista_aux[5])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]
            l_figura[aux + 5] = lista_aux[4]
            l_figura[aux + 6] = lista_aux[5]

        elif q_fig == 'rectangulo':

            aux = l_figura.index('rectangulo')
            lista_aux = transformacion.relexion_x([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4], l_figura[aux + 3], l_figura[aux + 2], l_figura[aux + 1], l_figura[aux + 4]])

            # ventana.limpiar()

            figura.rectangulo_4p(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3], lista_aux[4], lista_aux[5], lista_aux[6], lista_aux[7])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]

        elif q_fig == 'bezier':

            aux = l_figura.index('bezier')
            lista_aux = transformacion.relexion_x([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4], l_figura[aux + 5], l_figura[aux + 6], l_figura[aux + 7], l_figura[aux + 8]])

            #ventana.limpiar()

            curva.bezier(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3], lista_aux[4], lista_aux[5], lista_aux[6], lista_aux[7])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]
            l_figura[aux + 5] = lista_aux[4]
            l_figura[aux + 6] = lista_aux[5]
            l_figura[aux + 7] = lista_aux[6]
            l_figura[aux + 8] = lista_aux[7]

        menu_trans()

    elif opcion == '7': # Reflexion al eje Y
        q_fig = raw_input('\n\t¿Que figura desea reflejar en Y?')
        lista_aux = []
        if q_fig == 'linea':
            aux = l_figura.index('linea')
            lista_aux = transformacion.relexion_y([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4]])

            # ventana.limpiar()

            linea.add_entero(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]

        elif q_fig == 'circunferencia':

            aux = l_figura.index('circunferencia')
            lista_aux = transformacion.relexion_y([l_figura[aux + 1], l_figura[aux + 2]])

            # ventana.limpiar()

            circunferencia.bresenham(lista_aux[0], lista_aux[1], l_figura[aux + 3])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]

        elif q_fig == 'triangulo':

            aux = l_figura.index('triangulo')
            lista_aux = transformacion.relexion_y([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4], l_figura[aux + 5], l_figura[aux + 6]])

            # ventana.limpiar()

            figura.triangulo(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3], lista_aux[4], lista_aux[5])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]
            l_figura[aux + 5] = lista_aux[4]
            l_figura[aux + 6] = lista_aux[5]

        elif q_fig == 'rectangulo':

            aux = l_figura.index('rectangulo')
            lista_aux = transformacion.relexion_y([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4], l_figura[aux + 3], l_figura[aux + 2], l_figura[aux + 1], l_figura[aux + 4]])

            # ventana.limpiar()

            figura.rectangulo_4p(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3], lista_aux[4], lista_aux[5], lista_aux[6], lista_aux[7])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]

        elif q_fig == 'bezier':

            aux = l_figura.index('bezier')
            lista_aux = transformacion.relexion_y([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4], l_figura[aux + 5], l_figura[aux + 6], l_figura[aux + 7], l_figura[aux + 8]])

            #ventana.limpiar()

            curva.bezier(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3], lista_aux[4], lista_aux[5], lista_aux[6], lista_aux[7])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]
            l_figura[aux + 5] = lista_aux[4]
            l_figura[aux + 6] = lista_aux[5]
            l_figura[aux + 7] = lista_aux[6]
            l_figura[aux + 8] = lista_aux[7]

        menu_trans()

    elif opcion == '8': # Reflexion alrededor de  Y = X
        q_fig = raw_input('\n\t¿Que figura desea reflejar en Y=X?')
        lista_aux = []
        if q_fig == 'linea':
            aux = l_figura.index('linea')
            lista_aux = transformacion.relexion_y_igual_x([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4]])

            ventana.limpiar()

            linea.add_entero(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]

        elif q_fig == 'circunferencia':

            aux = l_figura.index('circunferencia')
            lista_aux = transformacion.relexion_y_igual_x([l_figura[aux + 1], l_figura[aux + 2]])

            # ventana.limpiar()

            circunferencia.bresenham(lista_aux[0], lista_aux[1], l_figura[aux + 3])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]

        elif q_fig == 'triangulo':

            aux = l_figura.index('triangulo')
            lista_aux = transformacion.relexion_y_igual_x([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4], l_figura[aux + 5], l_figura[aux + 6]])

            # ventana.limpiar()

            figura.triangulo(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3], lista_aux[4], lista_aux[5])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]
            l_figura[aux + 5] = lista_aux[4]
            l_figura[aux + 6] = lista_aux[5]

        elif q_fig == 'rectangulo':

            aux = l_figura.index('rectangulo')
            lista_aux = transformacion.relexion_y_igual_x([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4], l_figura[aux + 3], l_figura[aux + 2], l_figura[aux + 1], l_figura[aux + 4]])

            # ventana.limpiar()

            figura.rectangulo_4p(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3], lista_aux[4], lista_aux[5], lista_aux[6], lista_aux[7])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]

        elif q_fig == 'bezier':

            aux = l_figura.index('bezier')
            lista_aux = transformacion.relexion_y_igual_x([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4], l_figura[aux + 5], l_figura[aux + 6], l_figura[aux + 7], l_figura[aux + 8]])

            #ventana.limpiar()

            curva.bezier(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3], lista_aux[4], lista_aux[5], lista_aux[6], lista_aux[7])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]
            l_figura[aux + 5] = lista_aux[4]
            l_figura[aux + 6] = lista_aux[5]
            l_figura[aux + 7] = lista_aux[6]
            l_figura[aux + 8] = lista_aux[7]

        menu_trans()

    elif opcion == '9': # Reflexion alrededor de  Y = -X
        q_fig = raw_input('\n\t¿Que figura desea reflejar en Y=-X?')
        lista_aux = []
        if q_fig == 'linea':
            aux = l_figura.index('linea')
            lista_aux = transformacion.relexion_y_igual_menos_x([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4]])

            # ventana.limpiar()

            linea.add_entero(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]

        elif q_fig == 'circunferencia':

            aux = l_figura.index('circunferencia')
            lista_aux = transformacion.relexion_y_igual_menos_x([l_figura[aux + 1], l_figura[aux + 2]])

            # ventana.limpiar()

            circunferencia.bresenham(lista_aux[0], lista_aux[1], l_figura[aux + 3])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]

        elif q_fig == 'triangulo':

            aux = l_figura.index('triangulo')
            lista_aux = transformacion.relexion_y_igual_menos_x([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4], l_figura[aux + 5], l_figura[aux + 6]])

            # ventana.limpiar()

            figura.triangulo(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3], lista_aux[4], lista_aux[5])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]
            l_figura[aux + 5] = lista_aux[4]
            l_figura[aux + 6] = lista_aux[5]

        elif q_fig == 'rectangulo':

            aux = l_figura.index('rectangulo')
            lista_aux = transformacion.relexion_y_igual_menos_x([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4], l_figura[aux + 3], l_figura[aux + 2], l_figura[aux + 1], l_figura[aux + 4]])

            # ventana.limpiar()

            figura.rectangulo_4p(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3], lista_aux[4], lista_aux[5], lista_aux[6], lista_aux[7])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]

        elif q_fig == 'bezier':

            aux = l_figura.index('bezier')
            lista_aux = transformacion.relexion_y_igual_menos_x([l_figura[aux + 1], l_figura[aux + 2], l_figura[aux + 3], l_figura[aux + 4], l_figura[aux + 5], l_figura[aux + 6], l_figura[aux + 7], l_figura[aux + 8]])

            # ventana.limpiar()

            curva.bezier(lista_aux[0], lista_aux[1], lista_aux[2], lista_aux[3], lista_aux[4], lista_aux[5], lista_aux[6], lista_aux[7])
            l_figura[aux + 1] = lista_aux[0]
            l_figura[aux + 2] = lista_aux[1]
            l_figura[aux + 3] = lista_aux[2]
            l_figura[aux + 4] = lista_aux[3]
            l_figura[aux + 5] = lista_aux[4]
            l_figura[aux + 6] = lista_aux[5]
            l_figura[aux + 7] = lista_aux[6]
            l_figura[aux + 8] = lista_aux[7]

        menu_trans()

    elif opcion == '10':
        menu()


def menu():
    ################################
    # MENU PRINCIPAL DE PRIMITIVAS #
    ################################
    print('figuras : {}'.format(l_figura))

    ##################
    # Menú Principal #
    ##################
    print '------------------------------'
    # print '\n[1] Trazado de Líneas - METODO DIRECTO'
    # print '[2] Trazado de Líneas - METODO ADD SIMPLE'
    print '[1] Curva de Bezier'
    print '[3] Línea - ADD Entero'
    print '[4] Circunferencia - Bresenham'
    print '[5] Triangulo'
    print '[6] Rectángulo'


    print '\n[10] limpiar plano'
    print '[11] Salir\n'

    opcion = raw_input('opción : ')
    """
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
    """
    if opcion == '1':
        punto1 = raw_input('Punto 1 (x0 y0) : ')
        x0, y0 = separar_puntos(punto1)
        punto2 = raw_input('Punto 2 (x1 y1) : ')
        x1, y1 = separar_puntos(punto2)
        punto3 = raw_input('Punto 3 (x2 y2) : ')
        x2, y2 = separar_puntos(punto3)
        punto4 = raw_input('Punto 4 (x3 y3) : ')
        x3, y3 = separar_puntos(punto4)

        curva.bezier(x0, y0, x1, y1, x2, y2, x3, y3)
        l_figura.append('bezier')
        l_figura.append(x0)
        l_figura.append(y0)
        l_figura.append(x1)
        l_figura.append(y1)
        l_figura.append(x2)
        l_figura.append(y2)
        l_figura.append(x3)
        l_figura.append(y3)

        menu_trans()

    elif opcion == '3':
        punto1 = raw_input('Punto 1 (xi yi) : ')
        xi, yi = separar_puntos(punto1)
        punto2 = raw_input('Punto 2 (xf yf) : ')
        xf, yf = separar_puntos(punto2)

        linea.add_entero(xi, yi, xf, yf)
        l_figura.append('linea')
        l_figura.append(xi)
        l_figura.append(yi)
        l_figura.append(xf)
        l_figura.append(yf)

        menu_trans()

    elif opcion == '4':
        centro = raw_input('Centro (xc yc) : ')
        xc, yc = separar_puntos(centro)
        radio = int(raw_input('radio : '))
        circunferencia.bresenham(xc, yc, radio)
        l_figura.append('circunferencia')
        l_figura.append(xc)
        l_figura.append(yc)
        l_figura.append(radio)

        menu_trans()


    elif opcion == '5':
        punto1 = raw_input('Punto 1 (x1 y1) : ')
        x1, y1 = separar_puntos(punto1)
        punto2 = raw_input('Punto 2 (x2 y2) : ')
        x2, y2 = separar_puntos(punto2)
        punto3 = raw_input('Punto 3 (x3 y3) : ')
        x3, y3 = separar_puntos(punto3)

        figura.triangulo(x1, y1, x2, y2, x3, y3)

        l_figura.append('triangulo')
        l_figura.append(x1)
        l_figura.append(y1)
        l_figura.append(x2)
        l_figura.append(y2)
        l_figura.append(x3)
        l_figura.append(y3)

        menu_trans()

    elif opcion == '6':
        punto1 = raw_input('Punto 1 (x1 y1) : ')
        x1, y1 = separar_puntos(punto1)
        punto2 = raw_input('Punto 2 (x2 y2) : ')
        x2, y2 = separar_puntos(punto2)

        figura.rectangulo(x1, y1, x2, y2)

        l_figura.append('rectangulo')
        l_figura.append(x1)
        l_figura.append(y1)
        l_figura.append(x2)
        l_figura.append(y2)

        menu_trans()

    elif opcion == '10':
        ventana.limpiar()

        for i in range(0, len(l_figura)):
            l_figura.pop()

    elif opcion == '11':
        print '\nGracias :)'
        exit()


    menu()

#################################
# INICIO DEL PROGRAMA PRINCIPAL #
#################################

# lista de figuras del usuario
l_figura = []

ventana.titulo('AlvaroCAD')
ventana.ejes()
menu()
# mainloop()
