# coding=utf-8
from PyQt4 import Qt

__author__ = 'alvaro'

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import menu

##############################
# QtGui contiene los Widgets #
##############################


class Ventana(QWidget):
    def __init__(self):
        super(Ventana, self).__init__()

        # cambia el titulo de la ventana
        self.setWindowTitle('AlvaroCAD')

        # cambia el tamaño de la ventana
        self.resize(800, 600)
        ini = 1

    @staticmethod
    def pintar():
        print('hola')


    def paintEvent(self, QPaintEvent, ini=1):
        print('hola')
        if ini == 1:
            print('hola de nuevo')
            qp = QPainter()
            qp.begin(self)
            self.drawPoints(qp)
            qp.end()
            ini = 2
        else:
            pass

    def drawPoints(self, qp):
        qp.setPen(Qt.red)
        # size = self.size()

        for i in range(500):
            qp.drawPoint(i, i)

################################################
app = QApplication(sys.argv)

ventana = Ventana()
ventana.show()
ventana.pintar()

# mainloop que mantiene viva a la aplicacion
sys.exit(app.exec_())