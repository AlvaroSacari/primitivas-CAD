import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class endomess(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.draw = False

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:

            if self.draw == False:
                print('El punto inicial esta en : ', str(event.pos()))
                self.draw = True
                self.linePoints = []

            elif self.draw == True:
                print('El siguiente punto es : ', str(event.pos()))

            self.linePoints.append(event.pos())

        elif event.button() == Qt.RightButton:
            if self.draw == True:
                print('Con click derecho todos los punto son :', str(self.linePoints))
                self.draw = False

def main(argv):
    app = QApplication(argv, True)
    wnd = endomess()
    wnd.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main(sys.argv)
