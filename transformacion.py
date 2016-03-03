__author__ = 'alvaro'

import math


def traslacion(lista_puntos, tx, ty):
    # filas de la 1ra. matriz
    m = len(lista_puntos) / 2
    # columnas de la 1ra. matriz
    n = 3
    # filas de la 2da. matriz
    p = 3
    # columnas de la 2da matriz
    q = 3

    # poblando la 1ra. matriz
    matriz1 = []
    matriz2 = []
    matriz3 = []
    for i in range(m):
        matriz1.append([1] * n)

    for i in range(m):
        matriz3.append([1] * n)

    aux = 0
    for j in range(len(lista_puntos)):
        if j % 2 == 0:
            matriz1[aux][0] = lista_puntos[j]
        else:
            matriz1[aux][1] = lista_puntos[j]
            aux += 1

    for i in range(3):
        matriz2.append([0] * 3)

    matriz2[0][0], matriz2[1][1], matriz2[2][2] = 1, 1, 1
    matriz2[2][0], matriz2[2][1] = tx, ty

    for i in range(m):
        for j in range(q):
            matriz3[i][j] = 0
            for k in range(n):
                matriz3[i][j] = matriz3[i][j] + matriz1[i][k] * matriz2[k][j]

    lista =[]
    for i in range(m):
        for j in range(2):
            lista.append(matriz3[i][j])

    return lista


def rotacion(lista_puntos, tita):
    tita = tita * 3.14 / 180
    # filas de la 1ra. matriz
    m = len(lista_puntos) / 2
    # columnas de la 1ra. matriz
    n = 3
    # filas de la 2da. matriz
    p = 3
    # columnas de la 2da matriz
    q = 3

    # poblando la 1ra. matriz
    matriz1 = []
    matriz2 = []
    matriz3 = []
    for i in range(m):
        matriz1.append([1] * n)

    for i in range(m):
        matriz3.append([1] * n)

    aux = 0
    for j in range(len(lista_puntos)):
        if j % 2 == 0:
            matriz1[aux][0] = lista_puntos[j]
        else:
            matriz1[aux][1] = lista_puntos[j]
            aux += 1

    for i in range(3):
        matriz2.append([0] * 3)

    matriz2[0][0], matriz2[0][1], matriz2[1][0], matriz2[1][1], matriz2[2][2] = math.cos(tita), math.sin(tita), -math.sin(tita), math.cos(tita), 1

    for i in range(m):
        for j in range(q):
            matriz3[i][j] = 0
            for k in range(n):
                matriz3[i][j] = matriz3[i][j] + matriz1[i][k] * matriz2[k][j]

    lista =[]
    for i in range(m):
        for j in range(2):
            lista.append(int(matriz3[i][j]))

    return lista


# filas de la 1ra. matriz
    m = len(lista_puntos) / 2
    # columnas de la 1ra. matriz
    n = 3
    # filas de la 2da. matriz
    p = 3
    # columnas de la 2da matriz
    q = 3

    # poblando la 1ra. matriz
    matriz1 = []
    matriz2 = []
    matriz3 = []
    for i in range(m):
        matriz1.append([1] * n)

    for i in range(m):
        matriz3.append([1] * n)

    aux = 0
    for j in range(len(lista_puntos)):
        if j % 2 == 0:
            matriz1[aux][0] = lista_puntos[j]
        else:
            matriz1[aux][1] = lista_puntos[j]
            aux += 1

    for i in range(3):
        matriz2.append([0] * 3)

    matriz2[0][0], matriz2[1][1], matriz2[2][2] = 1, 1, 1
    matriz2[2][0], matriz2[2][1] = tx, ty

    for i in range(m):
        for j in range(q):
            matriz3[i][j] = 0
            for k in range(n):
                matriz3[i][j] = matriz3[i][j] + matriz1[i][k] * matriz2[k][j]

    lista =[]
    for i in range(m):
        for j in range(2):
            lista.append(matriz3[i][j])

    return lista


def escalamiento(lista_puntos, ex, ey):
    # filas de la 1ra. matriz
    m = len(lista_puntos) / 2
    # columnas de la 1ra. matriz
    n = 3
    # filas de la 2da. matriz
    p = 3
    # columnas de la 2da matriz
    q = 3

    # poblando la 1ra. matriz
    matriz1 = []
    matriz2 = []
    matriz3 = []
    for i in range(m):
        matriz1.append([1] * n)

    for i in range(m):
        matriz3.append([1] * n)

    aux = 0
    for j in range(len(lista_puntos)):
        if j % 2 == 0:
            matriz1[aux][0] = lista_puntos[j]
        else:
            matriz1[aux][1] = lista_puntos[j]
            aux += 1

    for i in range(3):
        matriz2.append([0] * 3)

    matriz2[0][0], matriz2[1][1], matriz2[2][2] = ex, ey, 1

    for i in range(m):
        for j in range(q):
            matriz3[i][j] = 0
            for k in range(n):
                matriz3[i][j] = matriz3[i][j] + matriz1[i][k] * matriz2[k][j]

    lista =[]
    for i in range(m):
        for j in range(2):
            lista.append(matriz3[i][j])

    return lista


def afilamiento_x(lista_puntos, afx):
    # filas de la 1ra. matriz
    m = len(lista_puntos) / 2
    # columnas de la 1ra. matriz
    n = 3
    # filas de la 2da. matriz
    p = 3
    # columnas de la 2da matriz
    q = 3

    # poblando la 1ra. matriz
    matriz1 = []
    matriz2 = []
    matriz3 = []
    for i in range(m):
        matriz1.append([1] * n)

    for i in range(m):
        matriz3.append([1] * n)

    aux = 0
    for j in range(len(lista_puntos)):
        if j % 2 == 0:
            matriz1[aux][0] = lista_puntos[j]
        else:
            matriz1[aux][1] = lista_puntos[j]
            aux += 1

    for i in range(3):
        matriz2.append([0] * 3)
    # matrix de transformacion:
    matriz2[0][0], matriz2[1][1], matriz2[2][2], matriz2[1][0] = 1, 1, 1, afx

    for i in range(m):
        for j in range(q):
            matriz3[i][j] = 0
            for k in range(n):
                matriz3[i][j] = matriz3[i][j] + matriz1[i][k] * matriz2[k][j]

    lista =[]
    for i in range(m):
        for j in range(2):
            lista.append(matriz3[i][j])

    return lista


def afilamiento_y(lista_puntos, afy):
    # filas de la 1ra. matriz
    m = len(lista_puntos) / 2
    # columnas de la 1ra. matriz
    n = 3
    # filas de la 2da. matriz
    p = 3
    # columnas de la 2da matriz
    q = 3

    # poblando la 1ra. matriz
    matriz1 = []
    matriz2 = []
    matriz3 = []
    for i in range(m):
        matriz1.append([1] * n)

    for i in range(m):
        matriz3.append([1] * n)

    aux = 0
    for j in range(len(lista_puntos)):
        if j % 2 == 0:
            matriz1[aux][0] = lista_puntos[j]
        else:
            matriz1[aux][1] = lista_puntos[j]
            aux += 1

    for i in range(3):
        matriz2.append([0] * 3)
    # matrix de transformacion:
    matriz2[0][0], matriz2[1][1], matriz2[2][2], matriz2[0][1] = 1, 1, 1, afy

    for i in range(m):
        for j in range(q):
            matriz3[i][j] = 0
            for k in range(n):
                matriz3[i][j] = matriz3[i][j] + matriz1[i][k] * matriz2[k][j]

    lista =[]
    for i in range(m):
        for j in range(2):
            lista.append(matriz3[i][j])

    return lista


def relexion_x(lista_puntos):
    # filas de la 1ra. matriz
    m = len(lista_puntos) / 2
    # columnas de la 1ra. matriz
    n = 3
    # filas de la 2da. matriz
    p = 3
    # columnas de la 2da matriz
    q = 3

    # poblando la 1ra. matriz
    matriz1 = []
    matriz2 = []
    matriz3 = []
    for i in range(m):
        matriz1.append([1] * n)

    for i in range(m):
        matriz3.append([1] * n)

    aux = 0
    for j in range(len(lista_puntos)):
        if j % 2 == 0:
            matriz1[aux][0] = lista_puntos[j]
        else:
            matriz1[aux][1] = lista_puntos[j]
            aux += 1

    for i in range(3):
        matriz2.append([0] * 3)
    # matrix de transformacion:
    matriz2[0][0], matriz2[1][1], matriz2[2][2] = 1, -1, 1

    for i in range(m):
        for j in range(q):
            matriz3[i][j] = 0
            for k in range(n):
                matriz3[i][j] = matriz3[i][j] + matriz1[i][k] * matriz2[k][j]

    lista =[]
    for i in range(m):
        for j in range(2):
            lista.append(matriz3[i][j])

    return lista


def relexion_y(lista_puntos):
    # filas de la 1ra. matriz
    m = len(lista_puntos) / 2
    # columnas de la 1ra. matriz
    n = 3
    # filas de la 2da. matriz
    p = 3
    # columnas de la 2da matriz
    q = 3

    # poblando la 1ra. matriz
    matriz1 = []
    matriz2 = []
    matriz3 = []
    for i in range(m):
        matriz1.append([1] * n)

    for i in range(m):
        matriz3.append([1] * n)

    aux = 0
    for j in range(len(lista_puntos)):
        if j % 2 == 0:
            matriz1[aux][0] = lista_puntos[j]
        else:
            matriz1[aux][1] = lista_puntos[j]
            aux += 1

    for i in range(3):
        matriz2.append([0] * 3)
    # matrix de transformacion:
    matriz2[0][0], matriz2[1][1], matriz2[2][2] = -1, 1, 1

    for i in range(m):
        for j in range(q):
            matriz3[i][j] = 0
            for k in range(n):
                matriz3[i][j] = matriz3[i][j] + matriz1[i][k] * matriz2[k][j]

    lista =[]
    for i in range(m):
        for j in range(2):
            lista.append(matriz3[i][j])

    return lista


def relexion_y_igual_x(lista_puntos):
    # filas de la 1ra. matriz
    m = len(lista_puntos) / 2
    # columnas de la 1ra. matriz
    n = 3
    # filas de la 2da. matriz
    p = 3
    # columnas de la 2da matriz
    q = 3

    # poblando la 1ra. matriz
    matriz1 = []
    matriz2 = []
    matriz3 = []
    for i in range(m):
        matriz1.append([1] * n)

    for i in range(m):
        matriz3.append([1] * n)

    aux = 0
    for j in range(len(lista_puntos)):
        if j % 2 == 0:
            matriz1[aux][0] = lista_puntos[j]
        else:
            matriz1[aux][1] = lista_puntos[j]
            aux += 1

    for i in range(3):
        matriz2.append([0] * 3)
    # matrix de transformacion:
    matriz2[0][1], matriz2[1][0], matriz2[2][2] = 1, 1, 1

    for i in range(m):
        for j in range(q):
            matriz3[i][j] = 0
            for k in range(n):
                matriz3[i][j] = matriz3[i][j] + matriz1[i][k] * matriz2[k][j]

    lista =[]
    for i in range(m):
        for j in range(2):
            lista.append(matriz3[i][j])

    return lista


def relexion_y_igual_menos_x(lista_puntos):
    # filas de la 1ra. matriz
    m = len(lista_puntos) / 2
    # columnas de la 1ra. matriz
    n = 3
    # filas de la 2da. matriz
    p = 3
    # columnas de la 2da matriz
    q = 3

    # poblando la 1ra. matriz
    matriz1 = []
    matriz2 = []
    matriz3 = []
    for i in range(m):
        matriz1.append([1] * n)

    for i in range(m):
        matriz3.append([1] * n)

    aux = 0
    for j in range(len(lista_puntos)):
        if j % 2 == 0:
            matriz1[aux][0] = lista_puntos[j]
        else:
            matriz1[aux][1] = lista_puntos[j]
            aux += 1

    for i in range(3):
        matriz2.append([0] * 3)
    # matrix de transformacion:
    matriz2[0][1], matriz2[1][0], matriz2[2][2] = -1, -1, 1

    for i in range(m):
        for j in range(q):
            matriz3[i][j] = 0
            for k in range(n):
                matriz3[i][j] = matriz3[i][j] + matriz1[i][k] * matriz2[k][j]

    lista =[]
    for i in range(m):
        for j in range(2):
            lista.append(matriz3[i][j])

    return lista


# matriz3 = traslacion([3, 4, 5, 6, 7, 8], 6, 15)
# matriz3 = rotacion([0, 20], 90)
# matriz3 = escalamiento([3, 4, 5, 6, 12, 14], 2, 3)
# matriz3 = afilamiento_x([3, 4, 5, 6, 12, 14], 2)
# print(matriz3)

