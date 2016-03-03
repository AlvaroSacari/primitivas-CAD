__author__ = 'alvaro'

import math
import pixel


def bezier(x0, y0, x1, y1, x2, y2, x3, y3):
    #d = 1.3 * (math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2) + math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) + math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2))
    d = (math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2) + math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) + math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2))
    t = 0.0
    while t < 1:
        xt = int((1 - t) ** 3 * x0 + 3 * t * (1 - t) ** 2 * x1 + 3 * t ** 2 * (1 - t) * x2 + t ** 3 * x3)
        yt = int((1 - t) ** 3 * y0 + 3 * t * (1 - t) ** 2 * y1 + 3 * t ** 2 * (1 - t) * y2 + t ** 3 * y3)
        pixel.pintar(xt, yt)
        t += (1 / d)


# bezier(-100, -80, -90, 70, 90, -70, 90, 100)