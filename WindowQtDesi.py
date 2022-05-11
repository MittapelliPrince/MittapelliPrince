from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic, QtGui
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Window.ui', self)
        self.setWindowIcon(QtGui.QIcon('C:\\users\\sentryeagle\\Desktop\\home.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
