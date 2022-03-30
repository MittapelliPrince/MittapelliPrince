from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My First Window')
        self.setGeometry(800, 200, 350, 340)
        self.menuBar = self.menuBar()
        fileMenu = self.menuBar.addMenu('File')

        self.CreateButton()

        self.show()

    def CreateButton(self):
        self.Button = QPushButton('Put Cursor Here', self)
        self.Button.setGeometry(125, 140, 100, 30)
        self.Button.setToolTip('<i><b>Click Button<b><i>')
        self.Button.clicked.connect(self.actionclicked)

    def actionclicked(self):
        print('Hello !')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = Window()
    sys.exit(app.exec())
